# Copyright

"""Classes representing date and time properties

As defined in :RFC:`5545`, section 3.8.2 (Date and Time Component
Properties).
"""

from . import base as _base


class DateTimeCompleted (_base.Property):
    ### RFC 5545, section 3.8.2.1 (Date-Time Completed)
    name = 'COMPLETED'
    parameters = ['TZID']
    dtypes = ['DATE-TIME']


class DateTimeEnd (_base.Property):
    ### RFC 5545, section 3.8.2.2 (Date-Time End)
    name = 'DTEND'
    parameters = ['TZID', 'VALUE']
    dtypes = ['DATE-TIME', 'DATE']


class DateTimeDue (_base.Property):
    ### RFC 5545, section 3.8.2.3 (Date-Time Due)
    name = 'DUE'
    parameters = ['TZID', 'VALUE']
    dtypes = ['DATE-TIME', 'DATE']


class DateTimeStart (_base.Property):
    ### RFC 5545, section 3.8.2.4 (Date-Time Start)
    name = 'DTSTART'
    parameters = ['TZID', 'VALUE']
    dtypes = ['DATE-TIME', 'DATE']


    ### RFC 5545, section 3.8.2.5 (Duration)
    ### RFC 5545, section 3.8.2.6 (Free/Busy Time)


class TimeTransparency (_base.Property):
    ### RFC 5545, section 3.8.2.7 (Time Transparency)
    name = 'TRANSP'
    dtypes = ['TEXT']
