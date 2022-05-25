#!/usr/bin/python3
# Copyright 2022 fnwinter@gmail.com

from requirements import req
from setuptools import setup, find_packages

VERSION = open("./cherrynas/config/version.txt").readline()

setup(name='cherrynas',
      version=VERSION,

      url='https://github.com/fnwinter/cherrynas',
      author='JungJik Lee',
      author_email='fnwinter@gmail.com',

      description='Installable NAS software',
      long_description='',

      packages=find_packages(),
      package_dir={'cherrynas': 'cherrynas'},

      zip_safe=False,
      install_requires=req,
      include_package_data=True
)