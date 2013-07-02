# Copyright

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
