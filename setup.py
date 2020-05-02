#!/usr/bin/env python
from setuptools import setup

setup(name='pytorch_wpe',
      version='0.0.0',
      description='A pytorch implementation of Weighted Prediction Error',
      url='https://github.com/nttcslab-sp/dnn_wpe',
      py_modules=['pytorch_wpe'],
      install_requires=['numpy', 'torch_complex'],
      setup_requires=[],
      tests_require=[]
      )
