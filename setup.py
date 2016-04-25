#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'IceCubeGameScheduleDataCollector',
    'author': 'Chad Paulinski',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose', 'urllib2', 'pytz', 'python-dateutil'],
    'packages': ['main'],
    'scripts': [],
    'name': 'IceCubeGameScheduleDataCollector'
}

setup(**config)
