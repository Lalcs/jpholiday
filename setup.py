# -*- coding: utf-8 -*-
from codecs import open
import os
import re
from setuptools import setup

with open(os.path.join('jpholiday', '__init__.py'), 'r', encoding='utf8') as f:
	version = re.compile(
		r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
	name='jpholiday',
	packages=['jpholiday'],
	version=version,
	license='MIT License',
	platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
	description='Pure-Python Japan Public Holiday Generate',
	author='Vatis',
	author_email='vatis@lalcs.com',
	url='https://github.com/Lalcs/jpholiday',
	keywords=['Japan', 'Holiday'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: Japanese',
		'Operating System :: MacOS',
		'Operating System :: Microsoft',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
	],
	data_files=[('', ['README.rst'])],
	long_description='{}'.format((open('README.rst', encoding='utf8').read())),
)