"""Module with basic errors to be used to define module specific errors.

Basic error types are defined here.

class Error
-----------

Basic error class with message and error string. Classes inheriting from
`Error` should specify an alternative `self.error_string` attribute to be
formatted into the string representation.

New subclasses can be defined as follows::

    class NewError(Error):
        # simple class docstring here

        def __init__(self, message):
            \"\"\"Construct error object.

            Parameters
            ----------
            message : str
                Message to be raised with error.

            \"\"\"
            super(NewError, self).__init__(message)
            self.error_string = 'NEW_ERROR'


"""
from __future__ import absolute_import
from __future__ import unicode_literals


__all__ = ["Error"]


class Error(Exception):
    """Generic custom exception to be extended by other exceptions."""

    def __init__(self, message: str):
        """Construct error object.

        Parameters
        ----------
        message : str
            Message to accompany error when it is raised.

        """
        super(Error, self).__init__(message)
        self.message = message
        self.error_string = "ERROR"

    def __str__(self) -> str:
        """Return string representation of error.

        Returns
        -------
        str
            Formatted string with error type and message.

        """
        return "[{}] {}".format(self.error_string, self.message)
