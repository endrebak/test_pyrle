
from distutils.core import setup, Extension
from setuptools import find_packages
from Cython.Build import cythonize

setup(name='rle',
      packages=find_packages(),
      ext_modules=cythonize("rle.pyx"), py_modules=["rle"],
      include_dirs=["."])


