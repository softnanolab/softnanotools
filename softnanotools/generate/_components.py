#!/usr/bin/env python
"""A module containing the common string-components found in Python files."""

from pathlib import Path

INDENT = "    "


class ComponentContainer:
    """Container for different components used in auto-generated Python files.

    Arguments:
        name: name of the file being generated (excluding .py)
    """

    shebang = "#!/usr/bin/env python"

    if_name_statement = "if __name__ == '__main__':"
    doctest_string = f"{INDENT}import doctest\n" f"{INDENT}doctest.testmod()"

    def __init__(self, name: str):
        name = Path(name)
        self._path = Path(name)
        self._name = self._path.name

    @property
    def name(self) -> str:
        split = self._name.split(".")
        if split[-1] == "py":
            name = ".".join(split[:-1])
        else:
            name = self._name
        return name

    @property
    def path(self) -> Path:
        return self._path.parent / f"{self.name}.py"

    @property
    def description(self) -> str:
        return f"{self.name}.py - auto-generated by softnanotools"

    @property
    def logger(self) -> str:
        return "from softnanotools.logger import Logger\n" "logger = Logger(__name__)\n"

    @property
    def docstring(self) -> str:
        return f'"""{self.description}"""'

    @property
    def parser(self) -> str:
        desc = self.description
        return (
            f"{INDENT}import argparse\n"
            f"{INDENT}parser = argparse.ArgumentParser(description='{desc}')\n"
            f"{INDENT}main(**vars(parser.parse_args()))\n"
        )

    @property
    def main_function(self) -> str:
        return (
            "def main(**kwargs):\n"
            f"{INDENT}logger.info('Running {self.name}...')\n"
            f"{INDENT}# insert code here\n"
            f"{INDENT}logger.info('Done!')\n"
            f"{INDENT}return\n"
        )


class FileContainer:
    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    import doctest

    doctest.testmod()
