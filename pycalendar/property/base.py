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

import io as _io
import itertools as _itertools

from .. import dtype as _dtype


class Property (dict):
    """An iCalendar property (e.g. VERSION)

    As defined in :RFC:`5545`, section 3.5 (Property).  Property names
    are defined in sections 3.7 (Calendar Properties) and 3.8
    (Component Properties).  Parameters are defined in section 3.2
    (Property Parameters), and value data types are defined in section
    3.3 (Property Value Data Types).
    """
    name = None
    parameters = []
    dtypes = []
    separator = None

    def __init__(self, parameters=None, value=None):
        if not parameters:
            parameters = {}
        super(Property, self).__init__()
        self.update(parameters)
        self.value = value

    def __hash__(self):
        return id(self)

    def __str__(self):
        with _io.StringIO() as stream:
            self.write(stream=stream, newline='\n')
            return stream.getvalue()[:-1]  # strip the trailing newline

    def __repr__(self):
        return '<{}.{} name:{} at {:#x}>'.format(
            self.__module__, type(self).__name__, self.name, id(self))

    def decode(self, value):
        dtype = self._get_dtype()
        return dtype.decode(property=self, value=value)

    def encode(self, value):
        dtype = self._get_dtype()
        return dtype.encode(property=self, value=value)

    def _get_dtype(self, dtype=None):
        if not dtype:
            if not self.dtypes:
                raise NotImplementedError('no default types for {!r}'.format(
                    self))
            dtype = self.get('VALUE', self.dtypes[0])
        if dtype not in self.dtypes:
            raise ValueError('invalid type {} for {!r}'.format(
                dtype, self.name))
        return _dtype.DTYPE[dtype]

    def check_parameters(self):
        for parameter in self.keys():
            if parameter not in self.parameters:
                raise ValueError(
                    'invalid parameter {} for {!r}'.format(parameter, self))

    def check_value(self):
        pass

    def write(self, stream, newline='\r\n', width=75):
        name_param = self.name
        line = '{}:{}'.format(
            ';'.join(_itertools.chain(
                [name_param],
                ['{}={}'.format(key, value)
                 for key,value in sorted(self.items())])),
            self.encode(self.value))
        lines = []
        if width:
            while len(line) > width:
                front = line[0:width]
                line = line[width:]
                if not lines:
                    width -= 1  # make room for the indent space
                else:
                    front = ' {}'.format(front)  # add the indent space
                lines.append(front)
            if lines:  # indent the last line
                line = ' {}'.format(line)
        lines.append(line)
        for line in lines:
            stream.write('{}{}'.format(line, newline))
