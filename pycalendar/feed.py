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

import codecs as _codecs
import logging as _logging
import urllib.request as _urllib_request

from . import USER_AGENT as _USER_AGENT
from . import property as _property
from . import unfold as _unfold
from .component import calendar as _calendar


_LOG = _logging.getLogger(__name__)


class Feed (_calendar.Calendar):
    r"""An iCalendar feed (:RFC:`5545`)

    Figure out where the example feed is located, relative to the
    directory from which you run this doctest (i.e., the project's
    root directory).

    >>> import os
    >>> root_dir = os.curdir
    >>> data_file = os.path.abspath(os.path.join(
    ...         root_dir, 'test', 'data', 'geohash.ics'))
    >>> url = 'file://{}'.format(data_file.replace(os.sep, '/'))

    Create a new feed pointing to this URL.

    >>> f = Feed(url=url)
    >>> f  # doctest: +ELLIPSIS
    <Feed url:file://.../test/data/geohash.ics>

    Load the feed content.

    >>> f.fetch()

    The ``.__str__`` method displays the feed content using Python's
    universal newlines.

    >>> print(f)  # doctest: +REPORT_UDIFF
    BEGIN:VCALENDAR
    PRODID:-//Example Calendar//NONSGML v1.0//EN
    VERSION:2.0
    BEGIN:VEVENT
    DTSTAMP:20130630T000000Z
    UID:2013-06-30@geohash.invalid
    DTSTART;VALUE=DATE:20130630
    GEO:42.226663;-71.286760
    LOCATION:Snow Hill\, Dover\, Massachusetts
    SUMMARY:XKCD geohashing\, Boston graticule
    URL:http://xkcd.com/426/
    DTEND;VALUE=DATE:20130701
    END:VEVENT
    END:VCALENDAR

    To get the CRLF line endings specified in :RFC:`5545`, use the
    ``.write`` method.

    >>> import io
    >>> stream = io.StringIO()
    >>> f.write(stream=stream)
    >>> stream.getvalue()  # doctest: +ELLIPSIS
    'BEGIN:VCALENDAR\r\nPRODID:...END:VCALENDAR\r\n'

    You can also iterate through events:

    >>> for event in f['VEVENT']:
    ...     print(repr(event))
    ...     print(event)
    ... # doctest: +ELLIPSIS, +REPORT_UDIFF
    <Event name:VEVENT at 0x...>
    BEGIN:VEVENT
    DTSTAMP:20130630T000000Z
    UID:2013-06-30@geohash.invalid
    DTSTART;VALUE=DATE:20130630
    GEO:42.226663;-71.286760
    LOCATION:Snow Hill\, Dover\, Massachusetts
    SUMMARY:XKCD geohashing\, Boston graticule
    URL:http://xkcd.com/426/
    DTEND;VALUE=DATE:20130701
    END:VEVENT
    """
    def __init__(self, url, user_agent=None):
        super(Feed, self).__init__(type='VCALENDAR')
        self.url = url
        if user_agent is None:
            user_agent = _USER_AGENT
        self.user_agent = user_agent

    def __repr__(self):
        return '<{}.{} url:{}>'.format(
            self.__module__, type(self).__name__, self.url)

    def fetch(self):
        self.clear()
        request = _urllib_request.Request(
            url=self.url,
            headers={
                'User-Agent': self.user_agent,
                },
            )
        with _urllib_request.urlopen(url=request) as f:
            info = f.info()
            content_type = info.get('Content-type', None)
            if content_type != 'text/calendar':
                raise ValueError(content_type)
            codec = _codecs.lookup('UTF-8')
            with codec.streamreader(stream=f) as stream:
                self.parse(stream=stream)

    def parse(self, stream):
        lines = _unfold.unfold(stream=stream)
        line = next(lines)
        prop = _property.parse(line=line)
        if prop.name != 'BEGIN' or prop.value != self.name:
            raise ValueError(
                "stream {} must start with 'BEGIN:VCALENDAR', not {!r}".format(
                    stream, line))
        self.read(lines=lines)
