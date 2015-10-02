"""HasItChanged
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
   name='hasItChanged',

   version='0.0.3',

   description='Monitor websites for changes',
   long_description=long_description,

   url='https://github.com/growdaisy/hasItChanged',

   author='Pokey Rule',
   author_email='pokey@growdaisy.com',

   license='MIT',

   classifiers=[
      'Development Status :: 3 - Alpha',

      'Intended Audience :: Developers',
      'Topic :: Communications :: Email',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
   ],

   keywords='email smtp sendgrid http',

   packages=find_packages(exclude=['contrib', 'docs', 'tests*',
                                   'examples']),

   install_requires=['requests', 'pyyaml'],

   entry_points={
      'console_scripts': [
         'hasItChanged = hasItChanged.__main__:main',
      ],
   },
)
