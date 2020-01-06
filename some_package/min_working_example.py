"""Module docstring.

Some additional text.

class ABC
---------

This header creates the problem.

class `DEF`
-----------

This header does not create a problem.

"""
from __future__ import absolute_import
from __future__ import unicode_literals


__all__ = ["ABC", "DEF"]


class ABC:
    """ABC class docstring."""

    def __init__(self):
        """Construct object."""
        self.name = "ABC"

class DEF:
    """DEF class docstring."""

    def __init__(self):
        """Construct object."""
        self.name = "DEF"

