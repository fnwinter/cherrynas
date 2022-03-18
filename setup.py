import pathlib
import pkg_resources

from setuptools import setup, find_packages

with pathlib.Path('./requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

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
      setup_requires=install_requires)