# -*- coding: utf-8 -*-
"""This is the main module of BeeDB library.

The main class is BeeDB which is responsible for creating connection.
"""


# this relies on each of the submodules having and __all__ variable set
from .beedb import *
from .error import *

__all__ = (beedb.__all__ +
           error.__all__)
