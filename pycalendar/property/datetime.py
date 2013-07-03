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

"""Classes representing date and time properties

As defined in :RFC:`5545`, section 3.8.2 (Date and Time Component
Properties).
"""

from . import base as _base


class DateTimeCompleted (_base.Property):
    ### RFC 5545, section 3.8.2.1 (Date-Time Completed)
    name = 'COMPLETED'
    parameters = ['TZID']
    dtypes = ['DATE-TIME']


class DateTimeEnd (_base.Property):
    ### RFC 5545, section 3.8.2.2 (Date-Time End)
    name = 'DTEND'
    parameters = ['TZID', 'VALUE']
    dtypes = ['DATE-TIME', 'DATE']


class DateTimeDue (_base.Property):
    ### RFC 5545, section 3.8.2.3 (Date-Time Due)
    name = 'DUE'
    parameters = ['TZID', 'VALUE']
    dtypes = ['DATE-TIME', 'DATE']


class DateTimeStart (_base.Property):
    ### RFC 5545, section 3.8.2.4 (Date-Time Start)
    name = 'DTSTART'
    parameters = ['TZID', 'VALUE']
    dtypes = ['DATE-TIME', 'DATE']


    ### RFC 5545, section 3.8.2.5 (Duration)
    ### RFC 5545, section 3.8.2.6 (Free/Busy Time)


class TimeTransparency (_base.Property):
    ### RFC 5545, section 3.8.2.7 (Time Transparency)
    name = 'TRANSP'
    dtypes = ['TEXT']
