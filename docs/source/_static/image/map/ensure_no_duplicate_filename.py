# -*- coding: utf-8 -*-

from collections import Counter
from pathlib_mate import Path

dir_here = Path.dir_here(__file__)

counter = Counter([
    p.fname
    for p in dir_here.select_image()
])

for key, count in counter.items():
    if count > 1:
        print(key)
