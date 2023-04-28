import softnanotools.notebooks._core as core

from pathlib import Path

PATH = (Path(__file__).parents[0] / '_assets').resolve()
NOTEBOOKS = [
    str(PATH / f'test-{i+1}.ipynb') for i in range(2)
]

def test_IPythonNotebook():
    core.IPythonNotebook(fname=NOTEBOOKS[0])
    return

def test_IPythonCell():
    core.IPythonCell()
    return
    