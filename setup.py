import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.RST')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.RST')) as f:
    CHANGES = f.read()

requires = [
    'pelican'
    ]

setup(name='pelican_cv',
      version='0.1.0',
      description='CV plugin for pelican using JSONResume',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        ],
      author='Mark Hall',
      author_email='mark.hall@work.room3b.eu',
      url='',
      keywords='pelican cv jsonresume',
      py_modules=['pelican_cv'],
      install_requires=requires,
      )
