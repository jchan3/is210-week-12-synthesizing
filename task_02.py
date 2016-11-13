#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 Synthesizing Task 02 docstring."""


class CustomError(Exception):
    """A Custom Exception object."""

    def __init__(self, message, cause):
        """Constructor for the CustomError cistom exception class.

        Args:
            message (string): The error message.
            cause (string): Reason for error.

        Attributes:
            cause (string): Reason for error.

        Examples:
            >>> myerr = CustomError('Whoah!', cause='Messed up!')
            >>> print myerr.cause
            Messed up!
        """
        self.cause = cause
        Exception.__init__(self, message)
