#!/usr/bin/env python
"""Generate a pytest suite with example test file."""
from pathlib import Path
from typing import List
from ._components import ComponentContainer
from softnanotools.logger import Logger
logger = Logger(__name__)

class TestContainer(ComponentContainer):
    def __init__(
        self, module: str, classes: List[str] = None, functions: List[str] = None
    ):
        if classes is None:
            self._classes = []
        else:
            self._classes = classes

        if functions is None:
            self._functions = []
        else:
            self._functions = classes

        self.module = module
        super().__init__(f"test_{module}")

    @property
    def imports(self) -> str:
        string = ""
        for c in self._classes:
            string.append(f"\t{c}\n")
        for f in self._functions:
            string.append(f"\t{f}\n")
        result = f"from {self.module} import (\n{string}\n)"
        return result

    @property
    def classes(self) -> str:
        result = ""
        for c in self._classes:
            result.append(f"def test_{c}():\n\treturn\n\n")
        return result

    @property
    def functions(self) -> str:
        result = ""
        for f in self._functions:
            result.append(f"def test_{f}():\n\treturn\n\n")
        return result

    @property
    def string(self) -> str:
        result = (
            f"{self.shebang}\n"
            f"{self.docstring}\n"
            f"{self.logger}\n"
            f"{self.imports}\n"
            f"{self.classes}\n"
            f"{self.functions}\n"
        )

        return result


class TestGenerator:
    """Reads the non-default classes and functions in a file, creates a test
    file, that imports all of them individually.
    """

    def __init__(self, module: str, folder: str = "test"):
        self.folder = Path(folder)
        self.folder.mkdir(exist_ok=True, parents=True)

        self.module = module
        self._classes = []
        self._functions = []

    def write(self):
        for c in self._classes:
            container = TestContainer(
                c, classes=self._classes, functions=self._functions
            )
            with open(self.folder / container.path, "w") as f:
                f.write(container.string)
        return


def generate(packages: List[str]):
    """Creates a directory called 'test', and iterates through each
    package, finds all of the nested packages and modules, and then
    creates a list of <package>.<module> strings, reads the functions
    and classes present in each <package>.<module> and creates tests
    for all of them, if they aren't already present.
    """
    return


if __name__ == "__main__":
    import doctest

    doctest.testmod()
