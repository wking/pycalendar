# Copyright

from . import base as _base


class TimeZone (_base.Component):
    """A time zone

    As defined in :RFC:`5545`, section 3.6.5 (Time Zone Component).
    """
    name = 'VTIMEZONE'
