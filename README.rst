============================================================================
pypidl - Download packages from PyPI indexes.
============================================================================

:Version: 0.0.1

Introduction
============

Library and command line application to download packages from PyPI.
The main reason for creating this is because `yolk`_ doesn't work with
custom PyPI index servers, and I have not, os of yet, received any reply
on the status of this bug.

.. _`yolk`: http://pypi.python.org/pypi/yolk

Installation
============

You can install ``pypidl`` either via the Python Package Index (PyPI)
or from source.

To install using ``pip``,::

    $ pip install pypidl


To install using ``easy_install``,::

    $ easy_install pypidl


If you have downloaded a source tarball you can install it
by doing the following,::

    $ python setup.py build
    # python setup.py install # as root

Examples
========

Command line examples
----------------------

Getting help::

    $ pypi_download --help

Download a package from a custom index server (also remove any existing local
files)::

    $ pypi_download --unlink -i http://chishop.example.com myapp
    myapp-0.4.2.tar.gz

Download a package with explicit version::

    $ pypi_download --version=0.4.1 yolk

Download package to custom destination directory::

    $ pypi_download --version=0.4.1 yolk --dest=/tmp


Library examples
----------------

Download a package from a custom index server (also remove any existing local
files):

    >>> from pypidl import download_package
    >>> download_package(package="myapp", directory=".", unlink=True,
    ...                  index="http://chishop.example.com")

    
Download a package with explicit version::

    >>> from pypidl import download_package
    >>> download_package(package="yolk", directory=".", unlink=True,
                         version="0.4.1")

Contact
-------

Ask Solem <askh@opera.com>

License
-------

BSD License
