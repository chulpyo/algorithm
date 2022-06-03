import click
from exceptions import common

@common.exception_handler(ValueError)
def handler(exc: ValueError):
    click.echo(f'value error -> {exc}')
    