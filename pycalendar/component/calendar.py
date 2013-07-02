# Copyright

from . import base as _base


class Calendar (_base.Component):
    """A calendar

    As defined in :RFC:`5545`, section 3.4 (iCalendar Object).
    """
    name = 'VCALENDAR'
    # contents defined in RFC 5545, section 3.6 (Calendar Components)
    required = [
        'PRODID',
        'VERSION',
        ]
    optional = [
        'CALSCALE',
        'METHOD',
        'X-PROP',
        'IANA-PROP',
        ]
    multiple = [
        'X-PROP',
        'IANA-PROP',
        ]
    subcomponents = [
        'VEVENT',
        'VTODO',
        'VJOURNAL',
        'VFREEBUSY',
        'VTIMEZONE',
        'VIANA-COMP',
        'VXCOMP',
        ]
