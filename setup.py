try:
    import setuptools
except ImportError:
    import distutils.core as setuptools

import beedb

setup(
    name='beedb',
    version=beedb.__version__,
    url='http://github.com/soltysh/beedb/',
    license=open('./LICENSE').read(),
    author='Maciej Szulik',
    author_email='soltysh@gmail.com',
    description='Engine that allows creating small, configurable databases'.
    long_description=open('./README.md').read(),
    packages=['beedb'],
    platforms='any',
    install_requires=open('./requirements.txt').read(),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent']
)

