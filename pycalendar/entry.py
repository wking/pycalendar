# Copyright

import logging as _logging

from . import text as _text


_LOG = _logging.getLogger(__name__)


class Entry (object):
    r"""An iCalendar entry (e.g. VEVENT)

    Get an entry.

    >>> from .feed import Feed

    >>> import os
    >>> root_dir = os.curdir
    >>> data_file = os.path.abspath(os.path.join(
    ...         root_dir, 'test', 'data', 'geohash.ics'))
    >>> url = 'file://{}'.format(data_file.replace(os.sep, '/'))

    >>> feed = Feed(url=url)
    >>> feed.fetch()
    >>> entry = feed.pop()

    Investigate the entry.

    >>> print(entry)
    BEGIN:VEVENT
    UID:2013-06-30@geohash.invalid
    DTSTAMP:2013-06-30T00:00:00Z
    DTSTART;VALUE=DATE:20130630
    DTEND;VALUE=DATE:20130701
    SUMMARY:XKCD geohashing\, Boston graticule
    URL:http://xkcd.com/426/
    LOCATION:Snow Hill\, Dover\, Massachusetts
    GEO:42.226663,-71.28676
    END:VEVENT

    >>> entry.type
    'VEVENT'
    >>> entry.content  # doctest: +ELLIPSIS
    'BEGIN:VEVENT\r\nUID:...\r\nEND:VEVENT\r\n'

    Use the ``.get*()`` methods to access individual fields.

    >>> entry.get('LOCATION')
    'Snow Hill\\, Dover\\, Massachusetts'
    >>> entry.get_text('LOCATION')
    'Snow Hill, Dover, Massachusetts'
    """
    def __init__(self, type, content=None):
        super(Entry, self).__init__()
        self.type = type
        self.content = content
        self.lines = None
        if content:
            self.process()

    def __str__(self):
        if self.content:
            return self.content.replace('\r\n', '\n').strip()
        return ''

    def __repr__(self):
        return '<{} type:{}>'.format(type(self).__name__, self.type)

    def process(self):
        self.unfold()

    def unfold(self):
        """Unfold wrapped lines

        Following :RFC:`5545`, section 3.1 (Content Lines)
        """
        self.lines = []
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
                    self.lines.append(''.join(semantic_line_chunks))
                semantic_line_chunks = [line]
        if semantic_line_chunks:
            self.lines.append(''.join(semantic_line_chunks))

    def get(self, key, **kwargs):
        for k in kwargs.keys():
            if k != 'default':
                raise TypeError(
                    'get() got an unexpected keyword argument {!r}'.format(
                        k))
        for line in self.lines:
            k,value = [x.strip() for x in line.split(':', 1)]
            if k == key:
                return value
        if 'default' in kwargs:
            return kwargs['default']
        raise KeyError(key)

    def get_text(self, *args, **kwargs):
        value = self.get(*args, **kwargs)
        return _text.unescape(value)

    def write(self, stream):
        stream.write(self.content)
