#!/usr/bin/env python3

from setuptools import setup

setup(
    name='distiller',
    version='0.0',
    description='Neural Network Distiller by Intel AI Lab',
    author='Neta Zmora and Guy Jacob and Gal Novik',
    url='https://github.com/NervanaSystems/distiller',
    packages=['distiller', 'apputils'],
    license='Apache License 2.0',
    install_requires=[
        'torch>=0.4.0',
        'numpy>=1.14.3',
        'torchvision>=0.2.1',
        'scipy>=1.1.0',
        'gitpython',
        'git+https://github.com/pytorch/tnt.git@master',
        'tensorflow>=1.7.0',
        'pydot>=1.2.4',
        'tabulate>=0.8.2',
        'pandas>=0.22.0',
        'jupyter>=1.0.0',
        'matplotlib>=2.2.2',
        'qgrid>=1.0.2',
        'graphviz>=0.8.2',
        'ipywidgets>=7.1.2',
        'bqplot>=0.10.5',
        'pyyaml',
        'pytest>=3.5.1',
    ]
)
