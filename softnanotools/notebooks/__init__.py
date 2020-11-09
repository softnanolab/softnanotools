"""
The `notebooks` module contains tools for importing and
scripting the generation of Jupyter Notebooks.

To a computer scientist Jupyter Notebooks are nothing 
but key:value objects that can be represented in a
number of ways. For example the YAML file format 
(which is a parent of JSON) can be used, or indeed its
child JSON, or XML ... Okay, these are about it.

In Python key:value objects are called dictionaries
and Jupyter Notebooks are dictionaries with some 
added rules, and so can be manipulated within Python.

classes:
    IPythonNotebook - notebook container
    IPythonCell - element in notebook
    IPythonTools - a class full of static methods

"""
from ._core import IPythonCell, IPythonNotebook, MARKDOWN, CODE
from ._utils import IPythonTools

merge = IPythonTools.merge
