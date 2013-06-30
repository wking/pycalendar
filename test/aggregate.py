#!/usr/bin/env python
#
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

"""An example aggregation script

This script grabs all the ``.ics`` files in the ``test/`` directory
and aggregates them into a single iCalendar feed.  While it's doing
this, it also prints and geographic positions to stderr.  In a live
site, you could use a different version of ``add_event`` to build
javascript that renders a map showing event locations.
"""

import os as _os
import sys as _sys

import pycalendar.aggregator as _pycalendar_aggregator
import pycalendar.feed as _pycalendar_feed


class Map (list):
    def __init__(self, stream=_sys.stderr):
        self.stream = stream

    def add_feed(self, feed):
        for event in feed['VEVENT']:
            self.add_event(event=event)

    def add_event(self, event):
        if 'GEO' in event:
            lat,lon = event.get_geo()
            self.stream.write('{} at lat {}, lon {}\n'.format(
                event['UID'], lat, lon))


def get_urls(root=_os.path.dirname(__file__)):
    for dirpath, dirnames, filenames in _os.walk(root):
        for filename in filenames:
            base,ext = _os.path.splitext(filename)
            if ext == '.ics':
                path = _os.path.abspath(_os.path.join(dirpath, filename))
                yield 'file://{}'.format(path.replace(_os.sep, '/'))


def aggregate(**kwargs):
    aggregator = _pycalendar_aggregator.Aggregator(
        prodid='-//pycalendar//NONSGML testing//EN',
        feeds=[_pycalendar_feed.Feed(url=url)
               for url in get_urls()],
        **kwargs)
    aggregator.fetch()
    return aggregator


if __name__ == '__main__':
    geomap = Map()
    aggregator = aggregate(processors=[geomap.add_feed])
    aggregator.write(stream=_sys.stdout)
