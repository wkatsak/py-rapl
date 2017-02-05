#!/usr/bin/python

from setuptools import setup

setup_info = dict(
	name="py-rapl",
	version="0.1",
	author="William Katsak",
	author_email="wkatsak@gmail.com",
	packages=["rapl"],
	zip_safe=True,
)

setup(**setup_info)
