# Copyright

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

    >>> a = Aggregator(
    ...     prodid='-//pycalendar//NONSGML testing//EN',
    ...     feeds=[
    ...         Feed(url='{}/{}'.format(base_url, name))
    ...         for name in ['geohash.ics',]],
    ...     )
    >>> a  # doctest: +ELLIPSIS
    [<Feed url:file://.../test/data/geohash.ics>]
    >>> a.fetch()

    Generate aggregate calendars with the ``.write`` method.

    >>> import io
    >>> stream = io.StringIO()
    >>> a.write(stream=stream)
    >>> value = stream.getvalue()
    >>> value  # doctest: +ELLIPSIS
    'BEGIN:VCALENDAR\r\nVERSION:2.0\r\n...END:VCALENDAR\r\n'
    >>> print(value.replace('\r\n', '\n'))
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//pycalendar//NONSGML testing//EN
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
    END:VCALENDAR
    <BLANKLINE>
    """
    def __init__(self, prodid, version='2.0', feeds=None):
        super(Aggregator, self).__init__()
        self.prodid = prodid
        self.version = version
        if feeds:
            self.extend(feeds)

    def fetch(self):
        for feed in self:
            feed.fetch()

    def write(self, stream):
        stream.write('BEGIN:VCALENDAR\r\n')
        stream.write('VERSION:{}\r\n'.format(self.version))
        stream.write('PRODID:{}\r\n'.format(self.prodid))
        for feed in self:
            for entry in feed:
                entry.write(stream=stream)
        stream.write('END:VCALENDAR\r\n')
