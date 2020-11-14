from pathlib import Path

import softnanotools.notebooks._utils as utils

PATH = (Path(__file__).parents[0] / '_assets').resolve()
NOTEBOOKS = [
    str(PATH / f'test-{i+1}.ipynb') for i in range(2)
]

def test_IPythonTools_merge():
    utils.IPythonTools.merge(NOTEBOOKS)
    return
    