from msilib.schema import Directory
import sys
import importlib
from pathlib import Path

def load_module(directory, name):
    sys.path.insert(directory[0])
    importlib.import_module(name)
    sys.path.pop([0])

def load_directory(directory):
    for path in directory:
        Path.rglob(".py")
        load_module(directory.as_posix(path.stem))

def loaded_bundled(self):
    directory = Path(__file__).parent / "extensions"
    self.loaded_directory(directory)