# setup.py

import io
from setuptools import setup, find_packages

setup(
    name='csv23',
    version='0.3.2',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Python 2/3 unicode CSV compatibility layer',
    keywords='unicode csv reader writer',
    license='MIT',
    url='https://github.com/xflr6/csv23',
    project_urls={
        'Documentation': 'https://csv23.readthedocs.io',
        'Changelog': 'https://csv23.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/xflr6/csv23/issues',
    },
    packages=find_packages(),
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    install_requires=[
        'mock; python_version < "3"',
    ],
    extras_require={
        'dev': ['tox>=3', 'flake8', 'pep8-naming', 'wheel', 'twine'],
        'test': ['mock>=3', 'pytest>=4.6', 'pytest-mock>=2', 'pytest-cov'],
        'docs': ['sphinx>=1.8', 'sphinx-rtd-theme'],
    },
    long_description=io.open('README.rst', encoding='utf-8').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
