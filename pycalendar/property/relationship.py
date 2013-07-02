# Copyright

"""Classes representing relationship properties

As defined in :RFC:`5545`, section 3.8.4 (Relationship Component
Properties).
"""

from . import base as _base


    ## RFC 5545, section 3.8.4 (Relationship Component Properties)
    ### RFC 5545, section 3.8.4.1 (Attendee)
    ### RFC 5545, section 3.8.4.2 (Contact)
    ### RFC 5545, section 3.8.4.3 (Organizer)
    ### RFC 5545, section 3.8.4.4 (Recurrence ID)
    ### RFC 5545, section 3.8.4.5 (Related To)


class UniformResourceLocator (_base.Property):
    ### RFC 5545, section 3.8.4.6 (Uniform Resource Locator)
    name = 'URL'
    dtypes = ['URI']


class UniqueIdentifier (_base.Property):
    ### RFC 5545, section 3.8.4.7 (Unique Identifier)
    name = 'UID'
    dtypes = ['TEXT']
