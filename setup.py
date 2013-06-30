# Copyright

"Flexible aggregation for iCalendar feeds (RFC 5545)"

import codecs as _codecs
from distutils.core import setup
import os.path as _os_path

from pycalendar import __version__, __url__


_name = 'pycalendar'
_this_dir = _os_path.dirname(__file__)


setup(
    name=_name,
    version=__version__,
    maintainer='W. Trevor King',
    maintainer_email='wking@tremily.us',
    url=__url__,
    download_url='https://github.com/wking/{}/archive/v{}.tar.gz'.format(
        _name, __version__),
    license='GNU General Public License v3 or later (GPLv3+)',
    platforms=['all'],
    description=__doc__,
    long_description=_codecs.open(
        _os_path.join(_this_dir, 'README'), 'r', encoding='utf-8').read(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    packages=[_name],
    provides=[_name],
    )
