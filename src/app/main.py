from email.policy import default
import os
import click

from functools import wraps
from typing import Callable, OrderedDict, TypeVar, Type
from typing_extensions import ParamSpec

_P = ParamSpec("_P")
_R = TypeVar("_R")

def test_deco(exception: Type[Exception] = Exception):
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


@click.group()
# @test_deco(exception=ValueError)
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f'running make-problem -> debug: {debug}')
    

@cli.command()
def make_problem() -> None:
    """문제 템플릿 자동 생성

    Parameters
    ----------
    
    Returns
    -------
    : None

    """

    # raise ValueError('fuck')
    click.echo('--')


if __name__ == '__main__':
    cli()
