# Copyright

"""Functions for processing numeric types

As defined in :RFC:`5545`, sections 3.3.7 (Float) and 3.3.8 (Integer).
"""

from . import base as _base


class Integer (_base.DataType):
    name = 'INTEGER'

    @classmethod
    def decode(cls, property, value):
        return int(value)

    @classmethod
    def encode(cls, property, value):
        return '{:d}'.format(value)


class Float (_base.DataType):
    name = 'FLOAT'

    @classmethod
    def decode(cls, property, value):
        return int(value)

    @classmethod
    def encode(cls, property, value):
        return '{:d}'.format(value)
