# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='nmt-metrics',

    version='0.1.0',

    description='A pure python implementation of multiple neural machine translation evaluation metrics',

    url='https://github.com/Belval/nmt-metrics',

    author='Edouard Belval',
    author_email='edouard@belval.org',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='nmt machine-translation translation metrics BLEU ROUGE METEOR',

    packages=find_packages(exclude=['contrib', 'docs']),
)
