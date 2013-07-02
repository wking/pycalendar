# Copyright

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
