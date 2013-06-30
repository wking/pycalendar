# Copyright

import logging as _logging


__version__ = '0.1'
__url__ = 'https://pypi.python.org/pypi/{}/'.format(__name__)

USER_AGENT = '{}/{} +{}'.format(__name__, __version__, __url__)

_LOG = _logging.getLogger(__name__)
_LOG.setLevel(_logging.WARNING)
_LOG.addHandler(_logging.StreamHandler())
