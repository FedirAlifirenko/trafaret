#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setupconf = dict(
    name = 'trafaret',
    version = '0.3.3',
    license = 'BSD',
    url = 'https://github.com/Deepwalker/trafaret/',
    author = 'Barbuza, Deepwalker',
    author_email = 'krivushinme@gmail.com',
    description = ('Validation and parsing library'),
    long_description = read('README.rst'),

    packages = find_packages(),

    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
    )

if __name__ == '__main__':
    setup(**setupconf)