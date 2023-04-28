"""Softnanotools Command-Line Interface (CLI)."""
import argparse
from typing import List
from . import _script, _module, _package, _project, _tests

from ..logger import Logger
logger = Logger(__name__)


def run(
    command: str,
    kind: str,
    name: str,
    modules: List[str] = None,
    packages: List[str] = None,
    dry_run: bool = False,
    pre_commit: bool = False,
    **kwargs
):
    """Run the softnanotools.[command] command from the terminal."""
    if modules is None:
        modules = []
    if packages is None:
        packages = []

    assert command == "generate"
    if kind == "script":
        _script.generate(name)
    elif kind == "module":
        _module.generate(name)
    elif kind == "package":
        _package.generate(name, modules=modules)
    elif kind == "tests":
        _tests.generate(name, packages=packages)
    elif kind == "project":
        _project.generate(
            name,
            packages=packages,
            modules=modules,
            dry_run=dry_run,
            pre_commit=pre_commit,
        )
    return


def main():
    """Run the softnanotools.[command] command from the terminal."""
    parser = argparse.ArgumentParser()
    parser.add_argument("kind")
    parser.add_argument("name")
    parser.add_argument("-m", "--modules", nargs="+")
    parser.add_argument("-p", "--packages", nargs="+")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="If you don't use this, `git init` and "
        "`pre-commit install` won't be run"
    )
    parser.add_argument(
        "--pre-commit",
        action="store_true",
        help="Add ruff auto-linting as a pre-commit"
    )
    args = parser.parse_args()
    run("generate", **vars(args))
    return
