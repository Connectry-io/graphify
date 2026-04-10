"""Tree-sitter grammar for Salesforce Apex — Python bindings.

Built from aheber/tree-sitter-sfapex (https://github.com/aheber/tree-sitter-sfapex).
Covers Apex, SOQL, and SOSL. The compiled shared library (apex.so) is loaded
via ctypes and exposed as a PyCapsule compatible with tree-sitter Python 0.25+.
"""
import ctypes
import os

_LIB_PATH = os.path.join(os.path.dirname(__file__), "apex.so")
_lib = ctypes.cdll.LoadLibrary(_LIB_PATH)
_lib.tree_sitter_apex.restype = ctypes.c_void_p

_PyCapsule_New = ctypes.pythonapi.PyCapsule_New
_PyCapsule_New.restype = ctypes.py_object
_PyCapsule_New.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]


def language():
    """Return the Apex language as a PyCapsule compatible with tree-sitter Python."""
    return _PyCapsule_New(_lib.tree_sitter_apex(), b"tree_sitter.Language", None)
