"""Jupyter and IPython Notebook Tools

Classes:
    IPythonTools: A collection of tools for manipulating IPython notebooks
"""
from ._core import IPythonCell, IPythonNotebook
from typing import List


class IPythonTools:
    """A container for tools for manipulating IPython Notebooks"""

    @staticmethod
    def merge(files: List[str], out: str = None, **kwargs):
        """Merge a list of IPython files

        Params:
            files: list of filepaths (useful with wildcards or globs)
            out: optional output file

        Returns:
            IPythonNotebook instance containing the merged cells
            from the list of filepaths

        Raises:
            AssertionError: if any standards are not met
        """
        output = IPythonNotebook()
        notebooks = []
        for fname in files:
            notebooks.append(IPythonNotebook(fname=fname))
            for cell in notebooks[-1].data["cells"]:
                if cell.get("outputs", None):
                    del cell["outputs"]
                if cell.get("execution_count", None):
                    del cell["execution_count"]
                output.data["cells"].append(vars(IPythonCell(cell)))
        if out:
            output.write(out)
        return output
