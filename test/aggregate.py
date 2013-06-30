#!/usr/bin/env python
#
# Copyright

"""An example aggregation script

This script grabs all the ``.ics`` files in the ``test/`` directory
and aggregates them into a single iCalendar feed.  While it's doing
this, it also prints and geographic positions to stderr.  In a live
site, you could use a different version of ``get_geo`` to build
javascript that renders a map showing event locations.
"""

import os as _os
import sys as _sys

import pycalendar.aggregator as _pycalendar_aggregator
import pycalendar.feed as _pycalendar_feed


def get_geo(feed):
    for event in feed['VEVENT']:
        if 'GEO' in event:
            lat,lon = [float(x) for x in event['GEO'].split(';')]
            _sys.stderr.write('{} at lat {}, lon {}\n'.format(
                event['UID'], lat, lon))


def get_urls(root=_os.path.dirname(__file__)):
    for dirpath, dirnames, filenames in _os.walk(root):
        for filename in filenames:
            base,ext = _os.path.splitext(filename)
            if ext == '.ics':
                path = _os.path.abspath(_os.path.join(dirpath, filename))
                yield 'file://{}'.format(path.replace(_os.sep, '/'))


def aggregate():
    aggregator = _pycalendar_aggregator.Aggregator(
        prodid='-//pycalendar//NONSGML testing//EN',
        feeds=[_pycalendar_feed.Feed(url=url)
               for url in get_urls()],
        processors=[get_geo],
        )
    aggregator.fetch()
    return aggregator


if __name__ == '__main__':
    aggregator = aggregate()
    aggregator.write(stream=_sys.stdout)
