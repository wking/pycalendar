# Copyright

class Feed (object):
    r"""An iCalendar feed (:RFC:`5545`)

    >>> f = Feed(url='http://example.com/calendar.ics')
    >>> f
    <Feed url:http://example.com/calendar.ics>
    >>> print(f)
    <BLANKLINE>

    We can't fetch this dummy url, so load the content by hand.

    >>> f.content = '\r\n'.join([
    ...         'BEGIN:VCALENDAR',
    ...         'VERSION:2.0',
    ...         'PRODID:-//Example Calendar//NONSGML v1.0//EN',
    ...         'BEGIN:VEVENT',
    ...         'UID:2013-06-30@geohash.invalid',
    ...         'DTSTAMP:2013-06-30T00:00:00Z',
    ...         'DTSTART;VALUE=DATE:20130630',
    ...         'DTEND;VALUE=DATE:20130701',
    ...         'SUMMARY:XKCD geohashing, Boston graticule',
    ...         'URL:http://xkcd.com/426/',
    ...         'LOCATION:Snow Hill, Dover, Massachusetts',
    ...         'GEO:42.226663,-71.28676',
    ...         'END:VEVENT',
    ...         'END:VCALENDAR',
    ...         '',
    ...         ])
    >>> print(f)
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//Example Calendar//NONSGML v1.0//EN
    BEGIN:VEVENT
    UID:2013-06-30@geohash.invalid
    DTSTAMP:2013-06-30T00:00:00Z
    DTSTART;VALUE=DATE:20130630
    DTEND;VALUE=DATE:20130701
    SUMMARY:XKCD geohashing, Boston graticule
    URL:http://xkcd.com/426/
    LOCATION:Snow Hill, Dover, Massachusetts
    GEO:42.226663,-71.28676
    END:VEVENT
    END:VCALENDAR

    To get the CRLF line endings specified in :RFC:`5545`, use the
    ``.write`` method.

    >>> import io
    >>> stream = io.StringIO()
    >>> f.write(stream=stream)
    >>> stream.getvalue()  # doctest: +ELLIPSIS
    'BEGIN:VCALENDAR\r\nVERSION:2.0\r\n...END:VCALENDAR\r\n'
    """
    def __init__(self, url, content=None):
        self.url = url
        self.content = content

    def __str__(self):
        if self.content:
            return self.content.replace('\r\n', '\n').strip()
        return ''

    def __repr__(self):
        return '<{} url:{}>'.format(type(self).__name__, self.url)

    def fetch(self):
        raise NotImplementedError()

    def write(self, stream):
        stream.write(self.content)
