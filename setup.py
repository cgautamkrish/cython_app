from distutils.core import setup
from Cython.Build import cythonize

setup(
	name = 'Gautam\'s App',
	ext_modules = cythonize("cython.pyx"),
)