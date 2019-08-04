# -*- coding: utf-8 -*-

import pandas as pd
from pathlib_mate import PathCls as Path
from wotlkdoc.df_to_list_table import df_to_list_table

p = Path(__file__).change(new_basename="Stat-Abbreviation.tsv")
df = pd.read_csv(p.abspath, sep="\t")
lt = df_to_list_table(df)
p = p.change(new_ext=".rst")
p.write_text(lt.render(), encoding="utf-8")
