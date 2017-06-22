#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from distutils.core import setup


	
if sys.argv[-1] == "publish":
	os.system("python setup.py sdist upload")
	sys.exit()

if sys.argv[-1] == "test":
	os.system("python test_ncbot.py")
	sys.exit()
	
required = []

# if python > 2.6, require simplejson

setup(
	name='ncbot',
	version='0.1.0',
	description='Awesome Python Library, that\'s NeteaseCloud`s Bot.',
	long_description=open('README.md').read(),
	author='XiyouMc',
	author_email='xiyoumc.dev@gmail.com',
	url='https://github.com/xiyoumc/ncbot',
	packages=[
		'ncbot',
		'ncbot.util'
	],
	install_requires=required,
	license='ISC',
	classifiers=(
		# 'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: ISC License (ISCL)',
		'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		# 'Programming Language :: Python :: 3.0',
		# 'Programming Language :: Python :: 3.1',
	),
)
