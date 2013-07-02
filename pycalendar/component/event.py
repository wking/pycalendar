# Copyright

from . import base as _base


class Event (_base.Component):
    """A calendar event

    As defined in :RFC:`5545`, section 3.6.1 (Event Component).
    """
    name = 'VEVENT'
    required=[
        'DTSTAMP',
        'UID',
        ]
    optional=[
        'DTSTART',  # required if VACLENDAR doesn't set METHOD
        # must not occur more than once
        'CLASS',
        'CREATED',
        'DESCRIPTION',
        'GEO',
        'LAST-MOD',
        'LOCATION',
        'ORGANIZER',
        'PRIORITY',
        'SEQUENCE',
        'STATUS',
        'SUMMARY',
        'TRANSP',
        'URL',
        'RECURID',
        # should not occur more than once
        'RRULE',
        # must not occur more than once
        'DTEND',
        'DURATION',  # but not when DTEND is also specified
        # may occur more than once
        'ATTACH',
        'ATTENDEE',
        'CATEGORIES',
        'COMMENT',
        'CONTACT',
        'EXDATE',
        'RSTATUS',
        'RELATED',
        'RESOURCES',
        'RDATE',
        'X-PROP',
        'IANA-PROP',
        ]
    multiple=[
        'ATTACH',
        'ATTENDEE',
        'CATEGORIES',
        'COMMENT',
        'CONTACT',
        'EXDATE',
        'RSTATUS',
        'RELATED',
        'RESOURCES',
        'RDATE',
        'X-PROP',
        'IANA-PROP',
        ]
