# Copyright

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
