# -*- coding: utf-8 -*-

"""
ConsoleMD parses markdown using CommonMark-py (implementation of the
CommonMarkdown spec) and then fully renders it to the console in true color.
"""

import os
from setuptools import setup

base_dir = os.path.dirname(os.path.abspath(__file__))
pkg_name = 'consolemd'

setup(
    name=pkg_name,
    packages=[pkg_name],

    install_requires=[
        'click<7.0',
        'pygments<3.0',
        'setproctitle<1.2',
        'commonmark<1.0',
    ],

    entry_points='''
        [console_scripts]
        consolemd=consolemd.cli:cli
    ''',

    # metadata for upload to PyPI
    description      = "ConsoleMD renders markdown to the console",
    long_description = __doc__,
    version          = '0.3.2',
    author           = 'Kurt Neufeld',
    author_email     = 'kneufeld@burgundywall.com',
    license          = 'MIT License',
    keywords         = "markdown console terminal".split(),
    url              = 'https://github.com/kneufeld/consolemd',

    classifiers      = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
        ],

    data_files       = [],
)
