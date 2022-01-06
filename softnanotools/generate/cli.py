import argparse
from typing import List

from ..logger import Logger
logger = Logger(__name__)

from . import _script, _module, _package, _project, _tests

def run(
    command: str,
    kind: str,
    name: str,
    modules: List[str] = None,
    packages: List[str] = None,
    github_actions: bool = False,
    tests: bool = False,
    **kwargs
):
    if modules == None:
        modules = []
    if packages == None:
        packages = []

    assert command == 'generate'
    if kind == 'script':
        _script.generate(name)
    elif kind == 'module':
        _module.generate(name)
    elif kind == 'package':
        _package.generate(name, modules=modules)
    elif kind == 'tests':
        _tests.generate(name, packages=packages)
    elif kind == 'project':
        _project.generate(
            name,
            packages=packages,
            modules=modules,
            github_actions=github_actions,
        )
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('kind')
    parser.add_argument('name')
    parser.add_argument('-m', '--modules', nargs='+')
    parser.add_argument('-p', '--packages', nargs='+')
    parser.add_argument('--github-actions', action='store_true')
    parser.add_argument('--tests', action='store_true')
    parser.add_argument('--code-cov', action='store_true')
    parser.add_argument('--no-versioneer', action='store_true')
    args = parser.parse_args()
    run('generate', **vars(args))
    return