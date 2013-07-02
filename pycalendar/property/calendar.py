# Copyright

"""Classes representing calendar properties

As defined in :RFC:`5545`, section 3.7 (Calendar Properties).
"""

from . import base as _base


class CalendarScale (_base.Property):
    ## RFC 5545, section 3.7.1 (Calendar Scale)
    name = 'CALSCALE'
    dtypes = ['TEXT']


class Method (_base.Property):
    ## RFC 5545, section 3.7.2 (Method)
    name = 'METHOD'
    dtypes = ['TEXT']


class ProductIdentifier (_base.Property):
    ## RFC 5545, section 3.7.3 (Product Identifier)
    name = 'PRODID'
    dtypes = ['TEXT']


class Version (_base.Property):
    ## RFC 5545, section 3.7.4 (Version)
    name = 'VERSION'
    dtypes = ['TEXT']

    def _check_value(self):
        if self.value != '2.0':
            raise NotImplementedError(
                'cannot parse {} {}'.format(self.name, self.value))
