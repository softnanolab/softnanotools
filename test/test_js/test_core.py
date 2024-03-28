from pathlib import Path
import softnanotools.js.core

FILE = Path(__file__).parent / '_assets' / 'test.json'

def test_JSONReader():
    JSONReader = softnanotools.js.core.JSONReader
    reader = JSONReader(FILE)
    assert reader.fname == FILE
    assert reader.data['user'] == "test"
    f2 = Path(__file__).parent / 'temp.json'
    reader.write(f2)
    reader2 = JSONReader(f2)
    assert reader.data['example']['nested'] == reader2.data['example']['nested']
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

def test_parse_key():
    key = 'user.name.first'
    keys = softnanotools.js.core.parse_key(key)
    assert keys == ['user', 'name', 'first']

def test_JSONReader_replace_nested():
    JSONReader = softnanotools.js.core.JSONReader
    fname = Path(__file__).parent / 'temp.json'
    JSONReader(FILE).write(fname)
    JSONReader.replace(fname, 'example.nested', 'temp')
    assert JSONReader(fname).data['example']['nested'] == 'temp'
    fname.unlink()
    return