# -*- coding: utf-8 -*-
"""
Module for NCryptoTools package distribution.
"""
from setuptools import setup, find_packages

setup(
    name='NCryptoTools',
    version='0.5.6',
    packages=find_packages(where='.', exclude=['test_*']),
    description='A set of tools needed for both NCryptoClient and NCryptoServer applications',
    author='Andrew Krylov',
    author_email='AndrewKrylovNegovsky@gmail.com',
    license='GNU General Public License v3.0',
    keywords=['JSON', 'Logger', 'Tools', 'FileManager', 'Utilities'],
)
