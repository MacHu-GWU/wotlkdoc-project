# -*- coding: utf-8 -*-

"""
Doc related file / folder paths
"""

import os
from pathlib_mate import Path


if "READTHEDOCS" in os.environ:
    dir_project_root = Path.cwd().parent.parent
else:
    dir_project_root = Path.dir_here(__file__).parent.parent

print("*******")
print(dir_project_root)
print(os.listdir(str(dir_project_root)))
assert (dir_project_root / "setup.py").exists()

dir_docs = dir_project_root / "docs"
dir_source = dir_docs / "source"
dir_static = dir_source / "_static"
