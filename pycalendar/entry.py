# Copyright

class Entry (object):
    """An iCalendar entry (e.g. VEVENT)
    """
    def __init__(self, type, content=None):
        self.type = type
        self.content = content

    def __str__(self):
        if self.content:
            return self.content.replace('\r\n', '\n').strip()
        return ''

    def __repr__(self):
        return '<{} type:{}>'.format(type(self).__name__, self.type)

    def write(self, stream):
        stream.write(self.content)
