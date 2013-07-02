# Copyright


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
