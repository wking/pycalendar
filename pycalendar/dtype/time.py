# Copyright

"""Functions for processing times without dates

As defined in :RFC:`5545`, section 3.3.12 (Time).
"""

import datetime as _datetime

import pytz as _pytz

from . import base as _base


class Time (_base.DataType):
    name = 'TIME'

    @classmethod
    def decode(cls, property, value):
        """Decode times without dates

        As defined in :RFC:`5545`, section 3.3.12 (Time).

        >>> Time.decode(property={}, value='230000')
        datetime.time(23, 0)
        >>> Time.decode(property={}, value='070000Z')
        datetime.time(7, 0, tzinfo=datetime.timezone.utc)
        >>> Time.decode(property={}, value='083000')
        datetime.time(8, 30)
        >>> Time.decode(property={}, value='133000Z')
        datetime.time(13, 30, tzinfo=datetime.timezone.utc)
        >>> Time.decode(property={'TZID': 'America/New_York'}, value='083000')
        ... # doctest: +NORMALIZE_WHITESPACE
        datetime.time(8, 30,
          tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)
        """
        tzinfo = property.get('TZID', None)
        if len(value) not in [6,7]:
            raise ValueError(value)
        hour = int(value[0:2])
        minute = int(value[2:4])
        second = int(value[4:6])
        if second == 60:  # positive leap second not supported by Python
            second = 59
        if value.endswith('Z'):
            tzinfo = _datetime.timezone.utc
        elif tzinfo:
            tzinfo = _pytz.timezone(tzinfo)
        return _datetime.time(
            hour=hour, minute=minute, second=second, tzinfo=tzinfo)

    @classmethod
    def encode(cls, property, value):
        if value.tzinfo == _datetime.timezone.utc:
            return value.strftime('%H%M%SZ')
        return value.strftime('%H%M%S')
