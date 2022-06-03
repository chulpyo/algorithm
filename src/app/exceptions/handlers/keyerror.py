import click
from exceptions import common
from typing import Type
@common.exception_handler(KeyError)
def handler(exc: Type[ValueError]):
    click.echo(f'key error -> {exc}')
    