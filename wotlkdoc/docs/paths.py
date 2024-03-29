# -*- coding: utf-8 -*-

"""
Doc related file / folder paths
"""

from pathlib_mate import Path

dir_project_root = Path.dir_here(__file__).parent.parent
assert (dir_project_root / "setup.py").exists()

dir_docs = dir_project_root / "docs"
dir_source = dir_docs / "source"
dir_static = dir_source / "_static"
