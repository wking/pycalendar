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

def _remove_newline(line):
    for newline in ['\r\n', '\n']:
        if line.endswith(newline):
            return line[:-len(newline)]
    raise ValueError('invalid line ending in {!r}'.format(line))


def unfold(stream):
    r"""Iterate through semantic lines, unfolding as neccessary

    Following :RFC:`5545`, section 3.1 (Content Lines).

    >>> import io
    >>> stream = io.StringIO('\r\n'.join([
    ...             'BEGIN:VCALENDER',
    ...             r'DESCRIPTION:Discuss how we can test c&s interoperability\n',
    ...             ' using iCalendar and other IETF standards.',
    ...             'ATTACH;FMTTYPE=text/plain;ENCODING=BASE64;VALUE=BINARY:VGhlIH'
    ...             ' F1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4',
    ...             '']))
    >>> for line in unfold(stream=stream):
    ...     print(repr(line))
    ... # doctest: +REPORT_UDIFF
    'BEGIN:VCALENDER'
    'DESCRIPTION:Discuss how we can test c&s interoperability\\nusing iCalendar and other IETF standards.'
    'ATTACH;FMTTYPE=text/plain;ENCODING=BASE64;VALUE=BINARY:VGhlIH F1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4'
    """
    semantic_line_chunks = []
    for line in stream:
        line = _remove_newline(line)
        lstrip = line.lstrip()
        if lstrip != line:
            if not semantic_line_chunks:
                raise ValueError(
                    ('whitespace-prefixed line {!r} is not a continuation '
                     'of a previous line').format(line))
            semantic_line_chunks.append(lstrip)
        else:
            if semantic_line_chunks:
                yield ''.join(semantic_line_chunks)
            semantic_line_chunks = [line]
    if semantic_line_chunks:
        yield ''.join(semantic_line_chunks)
