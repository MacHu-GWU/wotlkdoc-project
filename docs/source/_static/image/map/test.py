# -*- coding: utf-8 -*-

from pathlib_mate import Path

root = Path(
    "/Users/sanhehu/Documents/GitHub/wotlkdoc-project/docs/source/_static/image/currency"
)

for p in root.select_file():
    print(p)
    p.moveto(new_basename=p.basename.replace(" ", "-"))
