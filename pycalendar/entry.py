# Copyright (C) 2013 W. Trevor King <wking@tremily.us>
#
# This file is part of pycalender.
#
# pycalender is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pycalender is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# pycalender.  If not, see <http://www.gnu.org/licenses/>.

import logging as _logging

from . import text as _text


_LOG = _logging.getLogger(__name__)


class Entry (dict):
    r"""An iCalendar entry (e.g. VEVENT)

    Load example content.

    >>> import codecs
    >>> import os
    >>> root_dir = os.curdir
    >>> data_file = os.path.abspath(os.path.join(
    ...         root_dir, 'test', 'data', 'geohash.ics'))
    >>> with codecs.open(data_file, 'r', 'UTF-8') as f:
    ...     content = f.read()

    Make an entry.

    >>> calendar = Entry(content=content)

    Investigate the entry.

    >>> print(calendar)  # doctest: +REPORT_UDIFF
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//Example Calendar//NONSGML v1.0//EN
    BEGIN:VEVENT
    UID:2013-06-30@geohash.invalid
    DTSTAMP:2013-06-30T00:00:00Z
    DTSTART;VALUE=DATE:20130630
    DTEND;VALUE=DATE:20130701
    SUMMARY:XKCD geohashing\, Boston graticule
    URL:http://xkcd.com/426/
    LOCATION:Snow Hill\, Dover\, Massachusetts
    GEO:42.226663;-71.28676
    END:VEVENT
    END:VCALENDAR

    >>> calendar.type
    'VCALENDAR'

    ``Entry`` subclasses Python's ``dict``, so you can access raw
    field values in the usual ways.

    >>> calendar['VERSION']
    '2.0'
    >>> calendar.get('missing')
    >>> calendar.get('missing', 'some default')
    'some default'
    >>> sorted(calendar.keys())
    ['PRODID', 'VERSION', 'VEVENT']


    Dig into the children (which are always stored as lists):

    >>> event = calendar['VEVENT'][0]

    >>> event.type
    'VEVENT'
    >>> event.content  # doctest: +ELLIPSIS
    'BEGIN:VEVENT\r\nUID:...\r\nEND:VEVENT\r\n'
    >>> sorted(event.keys())
    ['DTEND', 'DTSTAMP', 'DTSTART', 'GEO', 'LOCATION', 'SUMMARY', 'UID', 'URL']

    >>> event['LOCATION']
    'Snow Hill\\, Dover\\, Massachusetts'

    You can also use ``get_text`` to unescape text fields.

    >>> event.get_text('LOCATION')
    'Snow Hill, Dover, Massachusetts'
    """
    def __init__(self, type=None, content=None):
        super(Entry, self).__init__()
        if type is None and content:
            firstline = content.splitlines()[0]
            type = firstline.split(':', 1)[1]
        self.type = type
        self.content = content
        self._lines = None  # unwrapped semantic lines
        if content:
            self.process()

    def __hash__(self):
        if self.type in [
                'VEVENT',
                'VFREEBUSY',
                'VJOURNAL',
                'VTODO',
                ] or 'UID' in self:
            return hash(_text.unescape(self['UID']))
        return id(self)

    def __str__(self):
        if self.content:
            return self.content.replace('\r\n', '\n').strip()
        return ''

    def __repr__(self):
        return '<{} type:{}>'.format(type(self).__name__, self.type)

    def process(self):
        self.unfold()
        self._parse()

    def _parse(self):
        self.clear()
        for index,verb,expected in [
                [0, 'begin', 'BEGIN:{}'.format(self.type)],
                [-1, 'end', 'END:{}'.format(self.type)],
                ]:
            if self._lines[index] != expected:
                raise ValueError('entry should {} with {!r}, not {!r}'.format(
                    verb, expected, self._lines[index]))
        stack = []
        child_lines = []
        for i,line in enumerate(self._lines[1:-1]):
            key,parameters,value = self._parse_key_value(line)
            if key == 'BEGIN':
                _LOG.debug('{!r}: begin {}'.format(self, value))
                stack.append(value)
            if stack:
                child_lines.append(line)
            if key == 'END':
                _LOG.debug('{!r}: end {}'.format(self, value))
                if not stack or value != stack[-1]:
                    raise ValueError(
                        ('closing {} on line {}, but current stack is {}'
                         ).format(value, i+1, stack))
                stack.pop(-1)
                if not stack:
                    child = Entry(
                        type=value,
                        content='\r\n'.join(child_lines) + '\r\n',
                        )
                    child._lines = child_lines
                    child._parse()
                    self._add_value(key=value, value=child, force_list=True)
                    child_lines = []
            elif not stack:  # our own data, not a child's
                if key == 'VERSION':
                    v = _text.unescape(value)
                    if v != '2.0':
                        raise NotImplementedError(
                            'cannot parse VERSION {} feed'.format(v))
                self._add_value(key=key, value=value)

    def _parse_key_value(self, line):
        key,value = [x.strip() for x in line.split(':', 1)]
        parameters = key.split(';')
        key = parameters.pop(0)
        parameters = {tuple(x.split('=', 1)) for x in parameters}
        for k,v in parameters:
            if ',' in v:
                parameters = v.split(',')
        if parameters and key in ['BEGIN', 'END']:
            raise ValueError(
                'parameters are not allowed with {}: {}'.format(
                    key, line))
        return (key, parameters, value)

    def _add_value(self, key, value, force_list=False):
        if force_list and key not in self:
            self[key] = []
        if key in self:
            if type(self[key]) == str:
                self[key] = [self[key]]
            self[key].append(value)
        else:
            self[key] = value

    def unfold(self):
        """Unfold wrapped lines

        Following :RFC:`5545`, section 3.1 (Content Lines)
        """
        self._lines = []
        semantic_line_chunks = []
        for line in self.content.splitlines():
            lstrip = line.lstrip()
            if lstrip != line:
                if not semantic_line_chunks:
                    raise ValueError(
                        ('whitespace-prefixed line {!r} is not a continuation '
                         'of a previous line').format(line))
                semantic_line_chunks.append(lstrip)
            else:
                if semantic_line_chunks:
                    self._lines.append(''.join(semantic_line_chunks))
                semantic_line_chunks = [line]
        if semantic_line_chunks:
            self._lines.append(''.join(semantic_line_chunks))

    def get_text(self, *args, **kwargs):
        """Get and unescape a text value

        As described in :RFC:`5545`, section 3.3.11 (Text)
        """
        value = self.get(*args, **kwargs)
        return _text.unescape(value)

    def get_geo(self, key='GEO', *args, **kwargs):
        """Get and unescape a GEO value

        As described in :RFC:`5545`, section 3.8.1.6 (Geographic
        Position).
        """
        value = self.get(key, *args, **kwargs)
        lat,lon = [float(x) for x in value.split(';')]
        return (lat, lon)

    def write(self, stream):
        stream.write(self.content)
