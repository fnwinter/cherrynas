import os
import sys
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_PATH)

from setuptools import setup, find_packages

from requirements import req

setup(name='cherrynas',
      version='0.0.1',
      url='https://github.com/fnwinter/cherrynas',
      author='JungJik Lee',
      author_email='fnwinter@gmail.com',
      description='Installable NAS software',
      packages=find_packages(),
      package_dir={'cherrynas': 'cherrynas'},
      long_description='',
      zip_safe=False,
      install_requires=req
)