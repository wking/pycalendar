# Copyright

"""Classes representing change management properties

As defined in :RFC:`5545`, section 3.8.7 (Change Management Component
Properties).
"""

from . import base as _base


    ## RFC 5545, section 3.8.7 (Change Management Component Properties)
    ### RFC 5545, section 3.8.7.1 (Date-Time Created)


class DateTimeStamp (_base.Property):
    ### RFC 5545, section 3.8.7.2 (Date-Time Stamp)
    name = 'DTSTAMP'
    dtypes = ['DATE-TIME']


    ### RFC 5545, section 3.8.7.3 (Last Modified)


class SequenceNumber (_base.Property):
    ### RFC 5545, section 3.8.7.4 (Sequence Number)
    name = 'SEQUENCE'
    dtypes = ['INTEGER']
