#!/usr/bin/python
# Copyright 2011-2012 John Dickinson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

from latency_middleware import __version__ as version


setup(
    name='latency_middleware',
    version=version,
    description='WSGI latency middlware',
    license='Apache License (2.0)',
    author='John Dickinson',
    author_email='me@not.mn',
    url='https://github.com/notmyname/latency_middleware',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
        ],
    entry_points={
        'paste.filter_factory': [
            'latency_middleware=latency_middleware.latency:filter_factory',
            ],
        },
    )
