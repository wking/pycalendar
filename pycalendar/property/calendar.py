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

As defined in :RFC:`5545`, section 3.7 (Calendar Properties).
"""

from . import base as _base


class CalendarScale (_base.Property):
    ## RFC 5545, section 3.7.1 (Calendar Scale)
    name = 'CALSCALE'
    dtypes = ['TEXT']


class Method (_base.Property):
    ## RFC 5545, section 3.7.2 (Method)
    name = 'METHOD'
    dtypes = ['TEXT']


class ProductIdentifier (_base.Property):
    ## RFC 5545, section 3.7.3 (Product Identifier)
    name = 'PRODID'
    dtypes = ['TEXT']


class Version (_base.Property):
    ## RFC 5545, section 3.7.4 (Version)
    name = 'VERSION'
    dtypes = ['TEXT']

    def _check_value(self):
        if self.value != '2.0':
            raise NotImplementedError(
                'cannot parse {} {}'.format(self.name, self.value))
