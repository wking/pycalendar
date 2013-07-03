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


class DataType (object):
    """Base class for processing data types

    As defined in :RFC:`5545`, section 3.3 (Property Value Data
    Types).
    """
    name = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<{}.{} name:{} at {:#x}>'.format(
            self.__module__, type(self).__name__, self.name, id(self))

    @classmethod
    def decode(cls, property, value):
        raise NotImplementedError('cannot decode {}'.format(cls))

    @classmethod
    def encode(cls, property, value):
        raise NotImplementedError('cannot encode {}'.format(cls))
