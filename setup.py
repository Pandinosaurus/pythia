#!/usr/bin/env python

from setuptools import setup

with open('pythia/version.py') as version_file:
    exec(version_file.read())

setup(name='pythia-learn',
      author='Matthew Spellings',
      author_email='mspells@umich.edu',
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Chemistry',
          'Topic :: Scientific/Engineering :: Physics'
      ],
      description='Machine learning fingerprints for particle environments',
      install_requires=['numpy', 'scipy', 'freud'],
      license='BSD',
      package_dir={'pythia': 'pythia'},
      packages=['pythia'],
      project_urls={
          'Documentation': 'http://pythia-learn.readthedocs.io/',
          'Source': 'https://bitbucket.org/glotzer/pythia'
      },
      python_requires='>=3',
      version=__version__
      )
