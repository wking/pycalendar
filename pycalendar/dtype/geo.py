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

"""Functions for processing geographic position

As defined in :RFC:`5545`, section 3.8.1.6 (Geographic Position).
"""

from . import base as _base


class Geo (_base.DataType):
    name = 'GEO'

    @classmethod
    def decode(cls, property, value):
        """Parse geographic position

        As defined in :RFC:`5545`, section 3.8.1.6 (Geographic
        Position).

        >>> Geo.decode(property={}, value='37.386013;-122.082932')
        (37.386013, -122.082932)
        """
        geo = tuple(float(x) for x in value.split(';'))
        if len(geo) != 2:
            raise ValueError(value)
        return geo

    @classmethod
    def encode(cls, property, value):
        return '{:.6f};{:.6f}'.format(*value)
