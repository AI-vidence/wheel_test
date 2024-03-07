from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [
    Extension(
        name="extension_name",
        sources= ["src/mypackage/secret_module.pyx"],
        #include_dirs=[...],
        #libraries=[...],
        #library_dirs=[...]),
    )
]

setup(
    name='mypackage',
    version='0.0.1',
    install_requires=[
        'pandas',
        'importlib-metadata; python_version>="3.10"',
    ],
    ext_modules=cythonize(extensions, compiler_directives={'language_level': 3}),
)