Latency Middleware
==================

Middlware that can simulate latency to a wsgi app. Total latency, request
latency, and response latency can all be set. If either the request or
response latency are set to empty (default), the value is understood to mean
half of the latency value.

How to Build to Debian Packages
===============================

    python setup.py --command-packages=stdeb.command bdist_deb
