# Copyright

import io as _io
import itertools as _itertools

from .. import property as _property
from .. import unfold as _unfold


_COMPONENT = {}


class Component (dict):
    r"""A base class for calendar components

    As defined in :RFC:`5545`, section 3.6 (Calendar Components).
    """
    name = None
    # properties
    required = []
    optional = []
    multiple = []
    # sub components
    subcomponents = []

    def __hash__(self):
        if self.name in [
                'VEVENT',
                'VFREEBUSY',
                'VJOURNAL',
                'VTODO',
                ] or 'UID' in self:
            return hash(self['UID'])
        return id(self)

    def __str__(self):
        with _io.StringIO() as stream:
            self.write(stream=stream, newline='\n')
            return stream.getvalue()[:-1]  # strip the trailing newline

    def __repr__(self):
        return '<{}.{} name:{} at {:#x}>'.format(
            self.__module__, type(self).__name__, self.name, id(self))

    def read(self, stream=None, lines=None):
        """Read an input stream and parse into properties and subcomponents
        """
        if lines is None:
            lines = _unfold.unfold(stream=stream)
        elif stream is not None:
            raise ValueError("cannot specify both 'stream' and 'lines'")
        for line in lines:
            prop = _property.parse(line)
            if prop.name == 'BEGIN':  # a subcomponent
                if prop.value not in self.subcomponents:
                    raise ValueError('invalid component {} for {!r}'.format(
                        prop.value, self))
                component_class = _COMPONENT[prop.value]
                component = component_class()
                component.read(lines=lines)
                self.add_component(component)
            elif prop.name == 'END':  # we're done with this component
                if prop.value != self.name:
                    raise ValueError('cannot close {!r} with {}'.format(
                        self, line))
                return
            else:  # a property
                self.add_property(property=prop)

    def add_component(self, component):
        name = component.name
        if name not in self.subcomponents:
            raise ValueError('invalid component {} for {!r}'.format(
                name, self))
        if name not in self:
            self[name] = []
        self[name].append(component)

    def add_property(self, property):
        name = property.name
        if name not in self.required and name not in self.optional:
            raise ValueError('invalid property {} for {!r}'.format(name, self))
        if name in self.multiple:
            if name not in self:
                self[name] = []
            self[name].append(property)
        else:
            self[name] = property

    def write(self, stream, newline='\r\n'):
        stream.write('BEGIN:{}{}'.format(self.name, newline))
        for prop in _itertools.chain(self.required, self.optional):
            self._write_property_by_name(
                name=prop, stream=stream, newline=newline)
        for component in self.subcomponents:
            self._write_component_by_name(
                name=component, stream=stream, newline=newline)
        stream.write('END:{}{}'.format(self.name, newline))

    def _write_component_by_name(self, name, stream, newline='\r\n'):
        component = self.get(name, [])
        if isinstance(component, list):
            for c in component:
                c.write(stream=stream, newline=newline)
        else:
            component.write(stream=stream, newline=newline)

    def _write_property_by_name(self, name, stream, newline='\r\n'):
        prop = self.get(name, [])
        if isinstance(prop, list):
            for p in prop:
                p.write(stream=stream, newline=newline)
        else:
            prop.write(stream=stream, newline=newline)
