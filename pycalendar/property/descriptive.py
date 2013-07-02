# Copyright

"""Classes representing descriptive component properties

As defined in :RFC:`5545`, section 3.8.1 (Descriptive Component
Properties).
"""

from . import base as _base


class Attachment (_base.Property):
    ### RFC 5545, section 3.8.1.1 (Attachment)
    name = 'ATTACH'
    dtypes = ['URI', 'BINARY']

    def _decode_value(self, property):
        type = property.parameters.get('VALUE', self.type)
        if type not in ['BINARY', 'URI']:
            raise ValueError('unregognized {} value: {}'.format(
                self.name, type))
        decoder = self.decoder or DECODER.get(self.type, None)
        if decoder:
            property.value = decoder(property=property)


class Categories (_base.Property):
    ### RFC 5545, section 3.8.1.2 (Categories)
    name = 'CATEGORIES'
    parameters = ['ALTREP']
    dtypes = ['TEXT']


class Classification (_base.Property):
    ### RFC 5545, section 3.8.1.3 (Classification)
    name = 'CLASSIFICATION'
    parameters = ['ALTREP']
    dtypes = ['TEXT']


class Comment (_base.Property):
    ### RFC 5545, section 3.8.1.4 (Comment)
    name = 'COMMENT'
    parameters = ['ALTREP']
    dtypes = ['TEXT']


class Description (_base.Property):
    ### RFC 5545, section 3.8.1.5 (Description)
    name = 'DESCRIPTION'
    parameters = ['ALTREP']
    dtypes = ['TEXT']


class GeographicPosition (_base.Property):
    ### RFC 5545, section 3.8.1.6 (Geographic Position)
    name = 'GEO'
    dtypes = ['GEO']


class Location (_base.Property):
    ### RFC 5545, section 3.8.1.7 (Location)
    name = 'LOCATION'
    parameters = ['ALTREP']
    dtypes = ['TEXT']


class PercentComplete (_base.Property):
    ### RFC 5545, section 3.8.1.8 (Percent Complete)
    name = 'PERCENT-COMPLETE'
    dtypes = 'INTEGER'


class Priority (_base.Property):
    ### RFC 5545, section 3.8.1.9 (Priority)
    name = 'PRIORITY'
    dtypes = ['INTEGER']


class Resources (_base.Property):
    ### RFC 5545, section 3.8.1.10 (Resources)
    name = 'RESOURCES'
    parameters = ['ALTREP']
    dtypes = ['TEXT']


class Status (_base.Property):
    ### RFC 5545, section 3.8.1.11 (Status)
    name = 'STATUS'
    parameters = ['ALTREP']
    dtypes = ['TEXT']


class Summary (_base.Property):
    ### RFC 5545, section 3.8.1.12 (Summary)
    name = 'SUMMARY'
    parameters = ['ALTREP']
    dtypes = ['TEXT']
