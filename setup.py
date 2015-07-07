#!/usr/bin/env python

from setuptools import setup


setup(
    name='make-deb',
    version='0.0.1',
    include_package_data = True,
    packages = ['make_deb'],
    package_data = {
        "make_deb": [
            "resources/debian/control.j2",
            "resources/debian/rules.j2",
            "resources/debian/triggers.j2",
            "resources/debian/changelog.j2",
            "resources/debian/compat.j2"
            ]
        },
    scripts=['bin/make-deb']
)