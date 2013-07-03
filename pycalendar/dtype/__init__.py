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

"""Classes for processing data types

As defined in :RFC:`5545`, section 3.3 (Property Value Data Types).
"""

from . import base as _base

from . import date as _date
from . import datetime as _datetime
from . import geo as _geo
from . import numeric as _numeric
from . import text as _text
from . import time as _time


DTYPE = {}


def register(dtype):
    DTYPE[dtype.name] = dtype


for module in [
        _date,
        _datetime,
        _geo,
        _numeric,
        _text,
        _time,
        ]:
    for name in dir(module):
        if name.startswith('_'):
            continue
        obj = getattr(module, name)
        if isinstance(obj, type) and issubclass(obj, _base.DataType):
            register(dtype=obj)
del module, name, obj
