from collections.abc import Callable
from typing import ParamSpec
from typing import TypeVar

__all__ = ["immediate"]

P = ParamSpec("P")
RT = TypeVar("RT")
MT = TypeVar("MT")

TT = TypeVar("TT", bound=type)


def immediate[RT](func: Callable[[], RT]) -> RT:
    """Immediately evaluate the given function, returning its output.

    >>> @immediate
    ... def VALUES():
    ...     return (0, 1)
    >>>
    >>> VALUES
    (0, 1)
    """
    return func()
