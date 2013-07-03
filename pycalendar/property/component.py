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

"""Classes representing calendar compenents

As defined in :RFC:`5545`, section 3.6 (Calendar Components).  These
aren't really properties, but the component parsing logic is simpler
if we pretend that they are.
"""

from . import base as _base


class BeginComponent (_base.Property):
    ## RFC 5545, section 3.6 (Calendar Components)
    name = 'BEGIN'
    dtypes = ['TEXT']


class EndComponent (_base.Property):
    ## RFC 5545, section 3.6 (Calendar Components)
    name = 'END'
    dtypes = ['TEXT']
