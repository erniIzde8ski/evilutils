"""Extensions upon the `functools` library."""

from functools import cache
from functools import cached_property
from functools import partial
from functools import partialmethod
from functools import wraps

from .compose import compose
from .decorators import immediate

__all__ = [
    "cache",
    "cached_property",
    "compose",
    "immediate",
    "partial",
    "partialmethod",
    "wraps",
]
