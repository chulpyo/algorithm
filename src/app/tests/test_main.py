from click.testing import CliRunner

from main import cli

def test_cli_make_problem_debug(cli_runner:CliRunner):
    result = cli_runner.invoke(cli, ['--debug', 'make-problem'])
    print(f'\n{result.output}')

def test_cli_make_problem_no_debug(cli_runner:CliRunner):
    result = cli_runner.invoke(cli, [ '--no-debug', 'make-problem'])
    print(f'\n{result.output}')
