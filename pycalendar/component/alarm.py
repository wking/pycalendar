# Copyright

from . import base as _base


class Alarm (_base.Component):
    """An alarm event

    As defined in :RFC:`5545`, section 3.6.6 (Alarm Component).
    """
    name = 'VALARM'
