#!/usr/bin/env python

from setuptools import setup

setup(name='ShigaTyper',
    version='2.0.1',
    description='Shigella serotype prediction tool',
    long_description=open('README.md').read(),
    author='Yun Wu, Henry Lau, Theresa Lee, David Lau, Justin Payne',
    author_email='Yun.Wu@fda.hhs.gov, Henry.Lau@fda.hhs.gov, Teresa.Lee@fda.hhs.gov, Justin.Payne@fda.hhs.gov',
    maintainer='Justin Payne',
    maintainer_email='Justin.Payne@fda.hhs.gov',
    url='https://github.com/CFSAN-Biostatistics/shigatyper',
    packages=['shigatyper'],
    data_files = [('resources', ['shigatyper/resources/ShigellaRef5.fasta','shigatyper/resources/ShigellaRef5.fasta.fai'])],
    include_package_data = True,
    license='USG work product released into the public domain',
    python_requires=">=3.7",
    install_requires=['pandas>=0.24',],
    entry_points=dict(console_scripts=['shigatyper = shigatyper.shigatyper:main',])
)
