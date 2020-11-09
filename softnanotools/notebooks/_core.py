"""Container for core classes IPythonNotebook, IPythonCell"""
import json

_NBFORMAT_ = 4
_NBFORMAT_MINOR_ = 4

_CELL_KEYS_ = (
    'cell_type',
    'metadata',
    'source',
    'execution_count',
    'outputs',
)

_MAIN_KEYS_ = (
    'cells',
    'metadata',
    'nbformat',
    'nbformat_minor',
)

_DEFAULT_METADATA_ = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    },
    "language_info": {
        "codemirror_mode": {
            "name": "ipython",
            "version": 3,
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.7.6",
    }
}

CODE = 'code'
MARKDOWN = 'markdown'

class IPythonCell:
    def __init__(self, cell: dict = None):
        if cell == None:
            self.cell_type = None
            self.metadata = {}
            self.source = []
            self.outputs = []
            self.execution_count = 0
        else:
            self.validate(cell)
            self.cell_type = cell['cell_type']
            self.metadata = cell['metadata']
            self.source = cell['source']
            self.outputs = cell.get('outputs', [])
            self.execution_count = cell.get('execution_count', 0)

        if self.cell_type == MARKDOWN:
            if hasattr(self, 'outputs'):
                del self.outputs
            if hasattr(self, 'execution_count'):
                del self.execution_count

    def validate(self, cell: dict):
        try:
            assert [i in _CELL_KEYS_ for i in cell.keys()]
        except AssertionError:
            raise TypeError(f'{cell.keys()} are not in {_CELL_KEYS_}')

        assert cell['cell_type'] in [MARKDOWN, CODE]
        assert isinstance(cell['metadata'], dict)
        assert isinstance(cell['source'], list)

class IPythonNotebook:
    """Notebook Container"""
    def __init__(self, fname: str = None):
        if fname:
            self.data = self.read(fname)
        else:
            self.data = {
                'cells' : [],
                'metadata' : {},
                'nbformat' : _NBFORMAT_,
                'nbformat_minor' : _NBFORMAT_MINOR_,
            }
        
        if self.data.get('metadata', {}) == {}:
            self.data['metadata'] = _DEFAULT_METADATA_

    def add_cell(
        self, 
        cell_type,
        source,
        metadata: dict = None
    ):
        cell = IPythonCell()
        
        # ensure cell type is correct
        assert cell_type in [CODE, MARKDOWN]
        cell.cell_type = cell_type

        # ensure source is a list
        assert isinstance(cell.source, list)
        cell.source = source
        if metadata:
            cell.metadata = metadata
        else:
            cell.metadata = {}
        cell.outputs = []
        cell.execution_count = 0
        self.data['cells'].append(vars(cell))
        return 

    def read(self, fname: str) -> dict:
        """Reads a IPython Notebook"""
        with open(fname, 'r') as f:
            data = json.load(f)
        
        self.validate(data)
        return data

    def write(self, fname: str):
        with open(fname, 'w') as f:
            json.dump(self.data, f, indent=2)
            f.write('\n')

    def validate(self, data: dict):
        """Checks that a IPython Notebook is of a valid format"""
        try:
            assert set(data.keys()) == set(_MAIN_KEYS_)
        except AssertionError:
            raise AssertionError(f"Notebook keys are {set(data.keys())} but should be {_MAIN_KEYS_}")
        assert isinstance(data['cells'], list)
        assert set(data['metadata']) == {
            'kernelspec',
            'language_info'
        }
        assert set(data['metadata']['kernelspec']) == {
            'display_name',
            'language',
            'name'
        }

        assert set(data['metadata']['language_info']) == {
            'codemirror_mode', 
            'file_extension', 
            'mimetype', 
            'name', 
            'nbconvert_exporter', 
            'pygments_lexer', 
            'version',
        }

        assert isinstance(data['nbformat'], int)
        assert isinstance(data['nbformat_minor'], int)
