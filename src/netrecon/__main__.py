#!/usr/bin/env python3
"""A rich CLI tool for network device reconnaissance."""
from datetime import datetime
from time import sleep
from typing import TYPE_CHECKING

import click

from rich.console import Console

from netrecon import __name__, __version__, __copyright__


if TYPE_CHECKING:
    from collections.abc import Callable

_version: str = f"{__name__} v{__version__} -- {__copyright__}"


@click.command()
@click.help_option("-h", "--help")
@click.version_option(__version__, "-v", "--version", message=_version)
def main() -> int:  # noqa: D103
    log_time_format: str = "[%Y-%m-%dT%H:%M:%S.%f%z]"
    get_datetime: Callable = lambda: datetime.now().astimezone()  # noqa: E731
    stdout: Console = Console(log_time_format=log_time_format, get_datetime=get_datetime)
    stderr: Console = Console(log_time_format=log_time_format, get_datetime=get_datetime, stderr=True)

    stderr.log("Started")
    with stdout.status("Working..."):
        sleep(3.0)
        stdout.print("[green]Hello [bold]World![/bold][/green]")
    stderr.log("Finished")

    return 0


if __name__ == "__main__":
    main()
