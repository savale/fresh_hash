from distutils.core import setup, Extension

fresh_hash_module = Extension('fresh_hash',
                   sources = ['freshmodule.c',
                              'fresh.c',
		              'sha3/shavite.c',
			      'sha3/simd.c',
                              'sha3/echo.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'fresh_hash',
       version = '1.1',
       description = 'Bindings for proof of work used by Fresh',
       ext_modules = [fresh_hash_module])
