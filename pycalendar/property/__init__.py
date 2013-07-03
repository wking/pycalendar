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

"""Classes representing calendar properties

As defined in :RFC:`5545`, sections 3.7 (Calendar Properties) and 3.8
(Component Properties).
"""

from . import base as _base

from . import alarm as _alarm
from . import calendar as _calendar
from . import change as _change
from . import component as _component
from . import datetime as _datetime
from . import descriptive as _descriptive
from . import misc as _misc
from . import recurrence as _recurrence
from . import relationship as _relationship
from . import timezone as _timezone


PROPERTY = {}


def register(property):
    """Register a property class
    """
    PROPERTY[property.name] = property


def parse(line):
    name_param,value = [x.strip() for x in line.split(':', 1)]
    parameters = name_param.split(';')
    name = parameters.pop(0).upper()  # names are case insensitive
    parameters = dict(tuple(x.split('=', 1)) for x in parameters)
    for k,v in parameters.items():
        if ',' in v:
            parameters[k] = v.split(',')
    prop_class = PROPERTY[name]
    prop = prop_class(parameters=parameters)
    prop.check_parameters()
    prop.value = prop.decode(value=value)
    prop.check_value()
    return prop


for module in [
        _alarm,
        _calendar,
        _change,
        _component,
        _datetime,
        _descriptive,
        _misc,
        _recurrence,
        _relationship,
        _timezone,
        ]:
    for name in dir(module):
        if name.startswith('_'):
            continue
        obj = getattr(module, name)
        if isinstance(obj, type) and issubclass(obj, _base.Property):
            register(property=obj)
del module, name, obj
