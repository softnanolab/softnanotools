from pathlib import Path
import softnanotools.js.core

FILE = Path(__file__).parent / '_assets' / 'test.json'

def test_JSONReader():
    JSONReader = softnanotools.js.core.JSONReader
    reader = JSONReader(FILE)
    assert reader.fname == FILE
    assert reader.data == {"user": "test"}
    f2 = Path(__file__).parent / 'temp.json'
    reader.write(f2)
    reader2 = JSONReader(f2)
    for key, value in reader2.data.items():
        assert value == reader.data[key]
    reader2.fname.unlink()
    return

def test_JSONReader_replace():
    JSONReader = softnanotools.js.core.JSONReader
    fname = Path(__file__).parent / 'temp.json'
    JSONReader(FILE).write(fname)
    JSONReader.replace(fname, 'user', 'temp')
    assert JSONReader(fname).data['user'] == 'temp'
    fname.unlink()
    return