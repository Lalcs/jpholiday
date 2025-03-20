import os
import re
from codecs import open

from setuptools import setup, find_packages

with open(os.path.join('jpholiday', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name='jpholiday',
    packages=find_packages(include=['jpholiday', 'jpholiday.*']),
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
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    data_files=[('', ['README.md'])],
    long_description='{}'.format((open('README.md', encoding='utf8').read())),
    long_description_content_type="text/markdown",
)
