from setuptools import setup
from Cython.Build import cythonize

setup(
    name='mypackage',
    version='0.0.2',
    install_requires=[
        'importlib-metadata; python_version>="3.11"',
    ],
    ext_modules=cythonize("src/secret.pyx", compiler_directives={'language_level': 3}),
)