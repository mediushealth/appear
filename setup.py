#!/usr/bin/env python

from distutils.core import setup

setup(
    name="appear",
    version="1.0",
    description="Make program internals appear in the browser",
    author="Andrew Houghton",
    author_email="houghtonandrew0@gmail.com",
    url="https://github.com/andrew-houghton/appear",
    packages=["appear"],
    long_description=open('README.md', 'r').read(),
    install_requires=['Flask-SocketIO', 'grequests'],
)
