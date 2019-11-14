# Welcome to the CreditScoring setup.py.
#
# To build

from __future__ import print_function
from codecs import open
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Get long description from the README file.
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='credit-scoring-toolkit',
    description='A Python package designed as a credit scoring toolkit.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.0.2',
    author='Liqiang Du',
    author_email='dlq137@gmail.com',
    url='https://github.com/Keris/creditscoring',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=[
        'finance',
        'credit',
        'scorecard',
        'regression',
        'machine learning',
    ],
    install_requires=[
        'matplotlib >= 1.1',
        'numpy >= 0.7.0',
        'pandas >= 0.20.1',
        'scipy >= 0.10.0',
        'seaborn >= 0.8.0',
        'scikit-learn >= 0.18'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'tools']),
    python_requires='>=3.6',
    test_suite="tests",
    tests_require=['pytest'],
    zip_safe=False
)