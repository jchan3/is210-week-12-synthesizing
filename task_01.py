#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 Synthesizing Task 01 docstring."""


class BaseError(Exception):
    """A Custom Exception object."""
    pass


class StringError(BaseError, TypeError):
    """A subclass of BaseError and TypeError."""
    pass


class NumberError(BaseError, TypeError):
    """A subclass of BaseError and TypeError."""
    pass


class NonZeroError(NumberError):
    """A subclass of NumberError."""
    pass
