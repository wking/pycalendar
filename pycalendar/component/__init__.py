# Copyright

"""Classes representing calendar components

As defined in :RFC:`5545`, section 3.6 (Calendar Components)

Usage
-----

Locate the example content.

>>> import codecs
>>> import os
>>> root_dir = os.curdir
>>> data_file = os.path.abspath(os.path.join(
...         root_dir, 'test', 'data', 'geohash.ics'))

Read a calendar.

>>> with codecs.open(data_file, 'r', 'UTF-8') as f:
...     calendar = parse(stream=f)

Investigate the entry.

>>> calendar.name
'VCALENDAR'

>>> for key,value in sorted(calendar.items()):
...     print((key, value))
... # doctest: +ELLIPSIS, +REPORT_UDIFF
('PRODID', <ProductIdentifier name:PRODID at 0x...>)
('VERSION', <Version name:VERSION at 0x...>)
('VEVENT', [<Event name:VEVENT at 0x...>])

>>> print(calendar)  # doctest: +REPORT_UDIFF
BEGIN:VCALENDAR
PRODID:-//Example Calendar//NONSGML v1.0//EN
VERSION:2.0
BEGIN:VEVENT
DTSTAMP:20130630T000000Z
UID:2013-06-30@geohash.invalid
DTSTART;VALUE=DATE:20130630
GEO:42.226663;-71.286760
LOCATION:Snow Hill\, Dover\, Massachusetts
SUMMARY:XKCD geohashing\, Boston graticule
URL:http://xkcd.com/426/
DTEND;VALUE=DATE:20130701
END:VEVENT
END:VCALENDAR

``Entry`` subclasses Python's ``dict``, so you can access raw
field values in the usual ways.

>>> calendar['VERSION'].value
'2.0'
>>> calendar.get('missing')
>>> calendar.get('missing', 'some default')
'some default'
>>> sorted(calendar.keys())
['PRODID', 'VERSION', 'VEVENT']

Dig into the subcomponents (which are always stored as lists):

>>> event = calendar['VEVENT'][0]

>>> event.name
'VEVENT'

>>> for key,value in sorted(calendar['VEVENT'][0].items()):
...     print((key, value))
... # doctest: +ELLIPSIS, +REPORT_UDIFF
('DTEND', <DateTimeEnd name:DTEND at 0x...>)
('DTSTAMP', <DateTimeStamp name:DTSTAMP at 0x...>)
('DTSTART', <DateTimeStart name:DTSTART at 0x...>)
('GEO', <GeographicPosition name:GEO at 0x...>)
('LOCATION', <Location name:LOCATION at 0x...>)
('SUMMARY', <Summary name:SUMMARY at 0x...>)
('UID', <UniqueIdentifier name:UID at 0x...>)
('URL', <UniformResourceLocator name:URL at 0x...>)

>>> event['LOCATION'].value
'Snow Hill, Dover, Massachusetts'
"""

from .. import property as _property
from .. import unfold as _unfold

from . import base as _base

from . import alarm as _alarm
from . import base as _base
from . import calendar as _calendar
from . import event as _event
from . import freebusy as _freebusy
from . import journal as _journal
from . import timezone as _timezone
from . import todo as _todo


COMPONENT = _base._COMPONENT


def register(component):
    """Register a component class
    """
    COMPONENT[component.name] = component


def parse(stream):
    """Load a single component from a stream
    """
    lines = _unfold.unfold(stream=stream)
    line = next(lines)
    prop = _property.parse(line=line)
    if prop.name != 'BEGIN':
        raise ValueError(
            "stream {} must start with 'BEGIN:...', not {!r}".format(
                stream, line))
    component_class = COMPONENT[prop.value]
    component = component_class()
    component.read(lines=lines)
    return component


for module in [
        _alarm,
        _base,
        _calendar,
        _event,
        _freebusy,
        _journal,
        _timezone,
        _todo,
        ]:
    for name in dir(module):
        if name.startswith('_'):
            continue
        obj = getattr(module, name)
        if isinstance(obj, type) and issubclass(obj, _base.Component):
            register(component=obj)
del module, name, obj
