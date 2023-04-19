#!/usr/bin/env python
"""_project.py - auto-generated by softnanotools."""
from typing import List
from pathlib import Path
from . import _package

from softnanotools.logger import Logger
logger = Logger(__name__)

ASSETS = Path(__file__).parent / "assets"

def generate(
    name,
    packages: List[str] = None,
    modules: List[str] = None,
    github_actions: bool = False,
    tests: bool = False,
    code_cov: bool = False,
    versioneer: bool = False,
    root=None,
):

    templates = {}

    # create folder with random string
    if root is None:
        root = Path(name)
    root.mkdir(exist_ok=True)

    # create main package
    _package.generate(root / name, modules=modules, packages=packages)

    # copy setup files from template area
    with open(ASSETS / "setup.py.template", "r") as f:
        templates["setup"] = f.read()

    with open(root / "setup.py", "w") as f:
        f.write(templates["setup"])

    # Add README.md
    with open(root / "README.md", "w") as f:
        f.write(f"# {name}\n")
        f.write("Generated by softnanotools!\n")

    # copy github actions from template area

    # copy code_cov template from template area

    # setup versioneer

    return


if __name__ == "__main__":
    import doctest

    doctest.testmod()
