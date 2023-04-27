#!/usr/bin/env python
"""_project.py - auto-generated by softnanotools."""
from typing import List, Union
from pathlib import Path
from . import _package

from softnanotools.logger import Logger
logger = Logger(__name__)

ASSETS = Path(__file__).parent / "assets"

def execute_template(fname: str, **kwargs) -> str:
    """Takes template from ASSETS folder and formats it with arguments"""
    # copy template from assets folder
    with open(ASSETS / f"{fname}.template", "r") as f:
        result = f.read()
        result = result.format(**kwargs)
    return result

def write_template(folder: Union[str, Path], fname: str, content: str):
    """Writes template to file in a project directory"""
    # write target file to dest
    with open(folder / fname, "w") as f:
        # write templated version with {subs} substitution rules
        f.write(content)

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

    # create test package
    _package.generate(root / 'test', modules=[f"test_{name}"])

    # create list of files to generate
    filenames = [
        "setup.py",
        "README.md",
        "setup.cfg",
        "_version.py",
        "MANIFEST.in",
        ".gitignore",
        "pyproject.toml"
    ]

    folders = {
        '_version.py': root / name
    }

    # loop over files
    for fname in filenames:
        # get templated string to write
        templates[fname] = execute_template(fname, name=name)

        # add debug statement
        logger.debug(templates[fname])

        # write template to file
        write_template(
            folders.get(fname, root), # use root folder if custom not specified
            fname,
            templates[fname]
        )



    return


if __name__ == "__main__":
    import doctest

    doctest.testmod()
