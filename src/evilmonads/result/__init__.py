"""All the monads I don't want to write twice."""

__all__ = ["Err", "Null", "Ok", "Option", "Result", "UnwrapError", "catch_unwind"]


from collections.abc import Callable
from dataclasses import dataclass
from functools import wraps

from .error import UnwrapError
from .variants import Err
from .variants import Null
from .variants import Ok
from .variants import Some

type Result[T, E: Exception] = Ok[T] | Err[E]
type Option[T] = Some[T] | Null


@dataclass
class catch_unwind[**P, T, E: Exception]:
    """Wraps a function and prevents it from raising the given exception(s)."""

    exc: type[E]

    def __call__(self, func: Callable[P, T]) -> Callable[P, Result[T, E]]:
        @wraps(func)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> Result[T, E]:
            try:
                res = func(*args, **kwargs)
                return Ok(res)
            except self.exc as exc:
                return Err(exc)

        return wrapped
