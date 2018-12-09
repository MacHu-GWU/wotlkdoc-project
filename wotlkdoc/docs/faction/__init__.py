# -*- coding: utf-8 -*-

import pandas as pd
from pathlib_mate import Path
from wotlkdoc.compressed_tsv import make_gzip, read_compressed_tsv
from wotlkdoc.df_to_list_table import df_to_list_table

tsv_filename = "faction.tsv"
make_gzip(this_file=__file__, filename=tsv_filename)
df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
df.columns = (
    "资料片,类型,名称,介绍,奖励,faction_id,到崇拜的GM命令"
).split(",")
df = df.drop(columns=["介绍",])

def construct_list_table(expansion):
    return df_to_list_table(
        df=df[df["资料片"]==expansion].copy().drop(columns=["资料片",]),
        title="{}声望".format(expansion),
        code_column_and_transform_func={
            "到崇拜的GM命令": None
        },
    )

lt_faction_vanilla = construct_list_table("经典旧世")
lt_faction_tbc = construct_list_table("燃烧的远征")
lt_faction_wlk = construct_list_table("巫妖王之怒")

if __name__ == "__main__":
    print(lt_faction_vanilla.render())
