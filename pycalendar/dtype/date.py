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

"""Functions for processing dates without times

As defined in :RFC:`5545`, section 3.3.4 (Date).
"""

import datetime as _datetime

from . import base as _base


class Date (_base.DataType):
    name = 'DATE'

    @classmethod
    def decode(cls, property, value):
        """Decode dates without times

        As defined in :RFC:`5545`, section 3.3.4 (Date).

        >>> Date.decode(property={}, value='19970714')
        datetime.date(1997, 7, 14)
        """
        if len(value) != 8:
            raise ValueError(value)
        year = int(value[0:4])
        month = int(value[4:6])
        day = int(value[6:8])
        return _datetime.date(year=year, month=month, day=day)

    @classmethod
    def encode(cls, property, value):
        return value.strftime('%Y%m%d')
