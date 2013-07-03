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

from . import base as _base


class Calendar (_base.Component):
    """A calendar

    As defined in :RFC:`5545`, section 3.4 (iCalendar Object).
    """
    name = 'VCALENDAR'
    # contents defined in RFC 5545, section 3.6 (Calendar Components)
    required = [
        'PRODID',
        'VERSION',
        ]
    optional = [
        'CALSCALE',
        'METHOD',
        'X-PROP',
        'IANA-PROP',
        ]
    multiple = [
        'X-PROP',
        'IANA-PROP',
        ]
    subcomponents = [
        'VEVENT',
        'VTODO',
        'VJOURNAL',
        'VFREEBUSY',
        'VTIMEZONE',
        'VIANA-COMP',
        'VXCOMP',
        ]
