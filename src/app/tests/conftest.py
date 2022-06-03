import pytest
import logging
from click.testing import CliRunner

@pytest.fixture
def cli_runner() -> logging.Logger:
    return CliRunner()
