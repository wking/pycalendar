# Copyright

from . import base as _base


class ToDo (_base.Component):
    """A to-do entry

    As defined in :RFC:`5545`, section 3.6.2 (To-Do Component).
    """
    name = 'VTODO'
