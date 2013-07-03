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


class Event (_base.Component):
    """A calendar event

    As defined in :RFC:`5545`, section 3.6.1 (Event Component).
    """
    name = 'VEVENT'
    required=[
        'DTSTAMP',
        'UID',
        ]
    optional=[
        'DTSTART',  # required if VACLENDAR doesn't set METHOD
        # must not occur more than once
        'CLASS',
        'CREATED',
        'DESCRIPTION',
        'GEO',
        'LAST-MOD',
        'LOCATION',
        'ORGANIZER',
        'PRIORITY',
        'SEQUENCE',
        'STATUS',
        'SUMMARY',
        'TRANSP',
        'URL',
        'RECURID',
        # should not occur more than once
        'RRULE',
        # must not occur more than once
        'DTEND',
        'DURATION',  # but not when DTEND is also specified
        # may occur more than once
        'ATTACH',
        'ATTENDEE',
        'CATEGORIES',
        'COMMENT',
        'CONTACT',
        'EXDATE',
        'RSTATUS',
        'RELATED',
        'RESOURCES',
        'RDATE',
        'X-PROP',
        'IANA-PROP',
        ]
    multiple=[
        'ATTACH',
        'ATTENDEE',
        'CATEGORIES',
        'COMMENT',
        'CONTACT',
        'EXDATE',
        'RSTATUS',
        'RELATED',
        'RESOURCES',
        'RDATE',
        'X-PROP',
        'IANA-PROP',
        ]
