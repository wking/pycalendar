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

"""Functions for processing dates with times

As defined in :RFC:`5545`, section 3.3.5 (Date-Time).
"""

import datetime as _datetime

from . import base as _base
from . import date as _date
from . import time as _time


class DateTime (_base.DataType):
    name = 'DATE-TIME'

    @classmethod
    def decode(cls, property, value):
        """Parse dates with times

        As defined in :RFC:`5545`, section 3.3.5 (Date-Time).

        >>> import pytz

        >>> DateTime.decode(property={}, value='19980118T230000')
        datetime.datetime(1998, 1, 18, 23, 0)
        >>> DateTime.decode(property={}, value='19980119T070000Z')
        datetime.datetime(1998, 1, 19, 7, 0, tzinfo=datetime.timezone.utc)

        The following represents 2:00 A.M. in New York on January 19,
        1998:

        >>> ny = {'TZID': 'America/New_York'}
        >>> DateTime.decode(property=ny, value='19980119T020000')
        ... # doctest: +NORMALIZE_WHITESPACE
        datetime.datetime(1998, 1, 19, 2, 0,
          tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)

        If, based on the definition of the referenced time zone, the local
        time described occurs more than once (when changing from daylight
        to standard time), the ``DATE-TIME`` value refers to the first
        occurrence of the referenced time.  Thus,
        ``TZID=America/New_York:20071104T013000`` indicates November 4,
        2007 at 1:30 A.M.  EDT (UTC-04:00).

        >>> DateTime.decode(property=ny, value='20071104T013000')
        ... # doctest: +NORMALIZE_WHITESPACE
        datetime.datetime(2007, 11, 4, 1, 30,
          tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)

        If the local time described does not occur (when changing from
        standard to daylight time), the ``DATE-TIME`` value is interpreted
        using the UTC offset before the gap in local times.  Thus,
        ``TZID=America/New_York:20070311T023000`` indicates March 11, 2007
        at 3:30 A.M. EDT (UTC-04:00), one hour after 1:30 A.M. EST
        (UTC-05:00).

        >>> DateTime.decode(property=ny, value='20070311T023000')
        ... # doctest: +NORMALIZE_WHITESPACE
        datetime.datetime(2007, 3, 11, 2, 30,
          tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)

        A time value MUST only specify the second 60 when specifying a
        positive leap second.  For example:

        >>> DateTime.decode(property={}, value='19970630T235960Z')
        datetime.datetime(1997, 6, 30, 23, 59, 59, tzinfo=datetime.timezone.utc)

        Implementations that do not support leap seconds SHOULD interpret
        the second 60 as equivalent to the second 59.

        The following represents July 14, 1997, at 1:30 PM in New York
        City in each of the three time formats

        >>> DateTime.decode(property={}, value='19970714T133000')
        datetime.datetime(1997, 7, 14, 13, 30)
        >>> d = DateTime.decode(property={}, value='19970714T173000Z')
        >>> d
        datetime.datetime(1997, 7, 14, 17, 30, tzinfo=datetime.timezone.utc)
        >>> d.astimezone(pytz.timezone('America/New_York'))
        ... # doctest: +NORMALIZE_WHITESPACE
        datetime.datetime(1997, 7, 14, 13, 30,
          tzinfo=<DstTzInfo 'America/New_York' EDT-1 day, 20:00:00 DST>)
        >>> DateTime.decode(property=ny, value='19970714T133000')
        ... # doctest: +NORMALIZE_WHITESPACE
        datetime.datetime(1997, 7, 14, 13, 30,
          tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)
        """
        date,time = value.split('T')
        date = _date.Date.decode(property=property, value=date)
        time = _time.Time.decode(property=property, value=time)
        return _datetime.datetime.combine(date=date, time=time)

    @classmethod
    def encode(cls, property, value):
        return '{}T{}'.format(
            _date.Date.encode(property=property, value=value.date()),
            _time.Time.encode(property=property, value=value.timetz()),
            )
