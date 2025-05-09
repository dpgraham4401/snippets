"""Utility functions for async_py.

See timed decorator https://gist.github.com/crizCraig/507e98a6ec6cecd0ed4db7170d540e2b.
"""

import asyncio
import time
from collections.abc import Callable
from typing import Any


def get_duration_str(start: float) -> str:
    """Get human-readable duration string from start time"""
    duration = time.time() - start
    if duration > 1:
        duration_str = f"{duration:,.3f}s"
    elif duration > 1e-3:
        duration_str = f"{round(duration * 1e3)}ms"
    elif duration > 1e-6:
        duration_str = f"{round(duration * 1e6)}us"
    else:
        duration_str = f"{duration * 1e9}ns"
    return duration_str


def timed(fn: Callable[..., Any]) -> Callable[..., Any]:
    def wrapped_fn(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        print(f"Running {fn.__name__}...")
        ret = fn(*args, **kwargs)
        duration_str = get_duration_str(start)
        print(f"Finished {fn.__name__} in {duration_str}")
        return ret

    async def wrapped_fn_async(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        print(f"Running {fn.__name__}...")
        ret = await fn(*args, **kwargs)
        duration_str = get_duration_str(start)
        print(f"Finished {fn.__name__} in {duration_str}")
        return ret

    if asyncio.iscoroutinefunction(fn):
        return wrapped_fn_async
    else:
        return wrapped_fn
