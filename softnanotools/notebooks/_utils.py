from ._core import IPythonCell, IPythonNotebook
from typing import List

class IPythonTools:
    """A container for tools for manipulating IPython Notebooks"""

    @staticmethod
    def merge(files: List[str], out: str = None, **kwargs):
        """Merge a list of IPython files"""
        output = IPythonNotebook()
        notebooks = []
        for fname in files:
            notebooks.append(IPythonNotebook(fname=fname))
            for cell in notebooks[-1].data['cells']:
                if cell.get('outputs', None):
                    del cell['outputs']
                if cell.get('execution_count', None):
                    del cell['execution_count']
                output.data['cells'].append(vars(IPythonCell(cell)))
        if out:
            output.write(out)
        return output
        