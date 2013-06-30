# Copyright (C) 2013 W. Trevor King <wking@tremily.us>
#
# This file is part of pycalender.
#
# pycalender is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pycalender is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# pycalender.  If not, see <http://www.gnu.org/licenses/>.

import logging as _logging


__version__ = '0.1'
__url__ = 'https://pypi.python.org/pypi/{}/'.format(__name__)

USER_AGENT = '{}/{} +{}'.format(__name__, __version__, __url__)

_LOG = _logging.getLogger(__name__)
_LOG.setLevel(_logging.WARNING)
_LOG.addHandler(_logging.StreamHandler())
