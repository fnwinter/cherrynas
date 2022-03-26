from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

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
      install_requires=[
            "Flask==2.0.2"
      ]
)