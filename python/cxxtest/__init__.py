#-------------------------------------------------------------------------
# CxxTest: A lightweight C++ unit testing library.
# Copyright (c) 2008 Sandia Corporation.
# This software is distributed under the LGPL License v2.1
# For more information, see the COPYING file in the top CxxTest directory.
# Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
# the U.S. Government retains certain rights in this software.
#-------------------------------------------------------------------------

"""cxxtest: A Python package that supports the CxxTest test framework for C/C++.

.. _CxxTest: http://cxxtest.tigris.org/

The _CxxTest testing framework is focussed on being a lightweight
framework that is well suited for integration into embedded systems
development projects.

CxxTest's advantages over existing alternatives are that it:

* Doesn't require RTTI
* Doesn't require member template functions
* Doesn't require exception handling
* Doesn't require any external libraries (including memory management, file/console I/O, graphics libraries)
* Is distributed entirely as a set of header files (and a python script).
* Doesn't require the user to manually register tests and test suites 

The cxxtest Python package includes capabilities for parsing C/C++ source files and generating
CxxTest drivers.
"""

from cxxtest.__release__ import __version__, __date__
__date__
__version__

__maintainer__ = "TODO"
__maintainer_email__ = "TODO"
__copyright__ = "TODO"
__license__ = "LGPL"
__url__ = "http://cxxtest.tigris.org/"

from cxxtest.cxxtestgen import *
