# Copyright

from . import base as _base


class Journal (_base.Component):
    """A journal entry

    As defined in :RFC:`5545`, section 3.6.3 (Journal Component).
    """
    name = 'VJOURNAL'
