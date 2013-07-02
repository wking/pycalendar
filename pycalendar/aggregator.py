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


from .component import calendar as _component_calendar
from .property import calendar as _property_calendar


class Aggregator (list):
    r"""An iCalendar feed aggregator

    Figure out where the example feeds are located, relative to the
    directory from which you run this doctest (i.e., the project's
    root directory).

    >>> import os
    >>> root_dir = os.curdir
    >>> data_dir = os.path.abspath(os.path.join(root_dir, 'test', 'data'))
    >>> base_url = 'file://{}'.format(data_dir.replace(os.sep, '/'))

    >>> from .feed import Feed

    You can set processing hooks to analyze and manipulate feeds as
    they come in.

    >>> processors = [lambda feed: print("I'm processing {!r}".format(feed))]

    >>> a = Aggregator(
    ...     prodid='-//pycalendar//NONSGML testing//EN',
    ...     feeds=[
    ...         Feed(url='{}/{}'.format(base_url, name))
    ...         for name in ['geohash.ics',]],
    ...     processors=processors,
    ...     )
    >>> a  # doctest: +ELLIPSIS
    [<Feed url:file://.../test/data/geohash.ics>]
    >>> a.fetch()  # doctest: +ELLIPSIS
    I'm processing <Feed url:file://.../test/data/geohash.ics>

    Generate aggregate calendars with the ``.write`` method.

    >>> import io
    >>> stream = io.StringIO()
    >>> a.write(stream=stream)
    >>> value = stream.getvalue()
    >>> value  # doctest: +ELLIPSIS
    'BEGIN:VCALENDAR\r\nPRODID:...END:VCALENDAR\r\n'
    >>> print(value.replace('\r\n', '\n'))  # doctest: +REPORT_UDIFF
    BEGIN:VCALENDAR
    PRODID:-//pycalendar//NONSGML testing//EN
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
    <BLANKLINE>
    """
    def __init__(self, prodid, version='2.0', feeds=None, processors=None):
        super(Aggregator, self).__init__()
        self.calendar = _component_calendar.Calendar()
        self.calendar.add_property(_property_calendar.Version(value=version))
        self.calendar.add_property(
            _property_calendar.ProductIdentifier(value=prodid))
        if feeds:
            self.extend(feeds)
        if not processors:
            processors = []
        self.processors = processors

    def fetch(self):
        for feed in self:
            feed.fetch()
            for processor in self.processors:
                processor(feed)
            for name in feed.subcomponents:
                if name not in self.calendar:
                    self.calendar[name] = []
                for component in feed.get(name, []):
                    self.calendar[name].append(component)

    def write(self, stream):
        self.calendar.write(stream=stream)
