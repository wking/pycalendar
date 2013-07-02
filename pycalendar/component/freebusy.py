# Copyright

from . import base as _base


class FreeBusy (_base.Component):
    """A request for, response to, or description of free/busy time

    As defined in :RFC:`5545`, section 3.6.4 (Free/Busy Component).
    """
    name = 'VFREEBUSY'
