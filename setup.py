#!/usr/bin/env python
'''Packaging Webgeocalc.'''

# This will try to import setuptools. If not here, it fails with a message
try:
    from setuptools import setup
except ImportError:
    raise ImportError("This module could not be installed, probably because"
                      " setuptools is not installed on this computer."
                      "\nInstall ez_setup ([sudo] pip install ez_setup) and try again.")

setup(
    setup_requires=['pbr'],
    pbr=True,
)
