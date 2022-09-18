# -*- coding: utf-8 -*-

"""
Doc related file / folder paths
"""

from pathlib_mate import Path
import os
for k, v in os.environ.items():
    print(k, v)
print(os.getcwd())
print(os.listdir(os.getcwd()))
dir_project_root = Path.dir_here(__file__).parent.parent
assert (dir_project_root / "setup.py").exists()

dir_docs = dir_project_root / "docs"
dir_source = dir_docs / "source"
dir_static = dir_source / "_static"
