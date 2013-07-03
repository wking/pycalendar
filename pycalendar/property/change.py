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

"""Classes representing change management properties

As defined in :RFC:`5545`, section 3.8.7 (Change Management Component
Properties).
"""

from . import base as _base


    ## RFC 5545, section 3.8.7 (Change Management Component Properties)
    ### RFC 5545, section 3.8.7.1 (Date-Time Created)


class DateTimeStamp (_base.Property):
    ### RFC 5545, section 3.8.7.2 (Date-Time Stamp)
    name = 'DTSTAMP'
    dtypes = ['DATE-TIME']


    ### RFC 5545, section 3.8.7.3 (Last Modified)


class SequenceNumber (_base.Property):
    ### RFC 5545, section 3.8.7.4 (Sequence Number)
    name = 'SEQUENCE'
    dtypes = ['INTEGER']
