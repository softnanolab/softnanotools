from typing import List

from softnanotools.notebooks import IPythonCell, IPythonNotebook, IPythonTools, CODE, MARKDOWN, merge

def create_notebook(fname: str):
    """Create a notebook with a single line
    """
    nb = IPythonNotebook()
    nb.add_cell(MARKDOWN, [f"# Test - {fname}"])
    nb.write(fname)
    return

def read_notebook(fname: str):
    """Read a notebook using the IPythonNotebook constructor
    """
    nb = IPythonNotebook(fname)
    return

def main():
    """Some examples of how to use the notebooks"""
    name = 'example-{}.ipynb'
    create_notebook(name.format(1))
    create_notebook(name.format(2))
    read_notebook(name.format(1))
    merge([
        name.format(1),
        name.format(2),
    ],
    out= name.format('merged'))
    return

if __name__ == '__main__':
    main()