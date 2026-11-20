__all__ = ["CapacityLimiter", "cache", "concurrency_limit", "open_file", "open_process"]

try:
    from anyio import CapacityLimiter
    from anyio import open_file
    from anyio import open_process
    from anyio.to_thread import run_sync
    from async_lru import alru_cache as cache
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Missing anyio module! Install `evilutils` with the `async` dependency group to fix this."
    )

from collections.abc import Awaitable
from collections.abc import Callable
from functools import partial
from functools import wraps


def concurrency_limit(n: int, /):
    """Limit a function to `n` concurrent invocations."""

    def limiter[**P, RT](fn: Callable[P, Awaitable[RT]]) -> Callable[P, Awaitable[RT]]:
        LIMIT = CapacityLimiter(n)

        @wraps(fn)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT:
            async with LIMIT:
                rv = await fn(*args, **kwargs)
            return rv

        return wrapper

    return limiter


async def to_thread[**P, RT](
    fn: Callable[P, RT], *args: P.args, **kwargs: P.kwargs
) -> RT:
    cb = partial(fn, *args, **kwargs)
    rv = await run_sync(cb)
    return rv


def to_threaded[**P, R](fn: Callable[P, R]) -> Callable[P, Awaitable[R]]:
    @wraps(fn)
    async def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
        return await to_thread(fn, *args, **kwargs)

    return wrapped
