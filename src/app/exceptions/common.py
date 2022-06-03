import click

from functools import wraps
from typing import Callable, OrderedDict, TypeVar
from typing_extensions import ParamSpec

_P = ParamSpec("_P")
_R = TypeVar("_R")

def exception_handler(exception: Exception = Exception):
    def decorator(f: Callable[_P, _R]) -> Callable[_P, _R]:
        """TEST 데코레이터"""
        @wraps(f)
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _R:
            try:
                result = f(*args, **kwargs)
            except exception as exc:
                result = None
                click.echo('????????????')
                click.echo(exc, err=True)
            
            return result
        return wrapper
    
    return decorator
