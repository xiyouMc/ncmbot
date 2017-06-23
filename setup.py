# -*- coding: utf-8 -*-
from __future__ import print_function  
from setuptools import setup, find_packages  
import sys  
import os
  
if sys.argv[-1] == "publish":
    os.system("python setup.py register sdist upload -r pypi")
    sys.exit()

if sys.argv[-1] == "test":
    os.system("python test_ncmbot.py")
    sys.exit()

setup(  
    name="ncmbot",  
    version="0.1.6",  
    author="XiyouMc",  
    author_email="xiyoumc.dev@gmail.com",  
    description="Awesome Python Library, that\'s NeteaseCloudMusic`s Bot.",  
    long_description=open("README.rst").read(),  
    license="ISC",  
    url="https://github.com/xiyoumc/ncmbot",  
    packages=['ncmbot', 'ncmbot.util'],
    install_requires=[  
        "requests",  
        'pycrypto'  
        ],  
    classifiers=[  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],  
)  






# import os
# import sys

# from distutils.core import setup



# required = ['requests', 'pycrypto']

# # if python > 2.6, require simplejson

# setup(
#     name='ncmbot',
#     version='0.1.4',
#     description='Awesome Python Library, that\'s NeteaseCloudMusic`s Bot.',
#     # long_description=open('README.md').read(),
#     author='XiyouMc',
#     author_email='xiyoumc.dev@gmail.com',
#     url='https://github.com/xiyoumc/ncmbot',
#     packages=['ncmbot', 'ncmbot.util'],
#     # install_requires=required,
#     license='ISC',
#     # classifiers=('Intended Audience :: Developers',
#     #              'Natural Language :: Chinese',
#     #              'License :: OSI Approved :: ISC License (ISCL)',
#     #              'Programming Language :: Python',
#     #              'Programming Language :: Python :: 2.6',
#     #              'Programming Language :: Python :: 2.7'),
#     # zip_safe=False, 
#     )
