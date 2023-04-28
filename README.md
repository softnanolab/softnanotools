# softnanotools

This repository contains a bunch of tools for different programming applications, mostly in Python. It is used through the [softnanolab](https://softnanolab.org/) research group

## Installation

The package uses only the Python standard library so the only prerequisite is the use of Python 3.

Installing using:

```sh
# pip
pip install softnanotools

# manual
git clone https://github.com/softnanolab/softnanotools
pip install ./softnanotools
```

## Modules

Here is a list of modules with a brief description:

- `notebooks` - Tools for manipulating Jupyter Notebooks
- `logger` - A logger that prints to screen
- `runner` - A tool for organising the execution of programs
- `generate` - A tool for generating python files and projects

## Usage

### `softnanotools.generate`
`softnanotools.generate` exists as a command-line interface (CLI) which can be called in the following
ways:

```sh
# Generate a simple python script called example.py
$ softnanotools.generate script example

# Generate a simple python module called example.py
$ softnanotools.generate module example

# Generate a package template called example using -m flag to specify internal module
$ softnanotools.generaet package example -m internal
$ tree example
example
├── __init__.py
└── internal.py

# Generate a package template called example using -m flag to specify internal module
$ softnanotools.generate package example -m internal.nested
$ tree example
example
├── __init__.py
└── internal
    ├── __init__.py
    └── nested.py

# Generate a full project and initialise with `git`
$ softnanotools.generate project example
$ tree example
example
├── .gitattributes
├── .github
│   └── workflows
│       ├── coverage.yml
│       └── quick-build.yml
├── .gitignore
├── MANIFEST.in
├── README.md
├── example
│   ├── __init__.py
│   └── _version.py
├── pyproject.toml
├── setup.cfg
├── setup.py
├── test
│   ├── __init__.py
│   └── test_example.py
└── versioneer.py
```
