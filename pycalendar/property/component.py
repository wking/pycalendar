# Copyright

"""Classes representing calendar compenents

As defined in :RFC:`5545`, section 3.6 (Calendar Components).  These
aren't really properties, but the component parsing logic is simpler
if we pretend that they are.
"""

from . import base as _base


class BeginComponent (_base.Property):
    ## RFC 5545, section 3.6 (Calendar Components)
    name = 'BEGIN'
    dtypes = ['TEXT']


class EndComponent (_base.Property):
    ## RFC 5545, section 3.6 (Calendar Components)
    name = 'END'
    dtypes = ['TEXT']
