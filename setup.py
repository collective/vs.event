# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.9.0.dev0'

setup(
    name='vs.event',
    version=version,
    description=(
        "An extended event content-type for Plone (and Plone4Artists calendar)"
    ),
    long_description=(
        open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Zope Plone Event Recurrence Calendar Plone4Artists',
    author='Veit Schiele, Anne Walther, Andreas Jung',
    author_email='vs.event@veit-schiele.de',
    url='https://github.com/collective/vs.event',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['vs'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.DataGridField',
        'collective.calendarwidget',
        'dateable.chronos',
        'dateable.kalends',
        'python-dateutil',
    ],
    extras_require={
        'tests': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
    },
    entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
