# -*- coding: utf-8 -*-

import polars as pl

from ..importer import (
    TsvGzReader,
    dataframe_to_list_table,
)
from .go_cmd import with_teleport_command


def lt_list_common_gps():
    reader = TsvGzReader(__file__)
    df = reader.read_df("common.tsv.gz")
    df = df.select([
        pl.col("name").alias("地点"),
        pl.col("go_cmd"),
    ])
    df = with_teleport_command(df, go_cmd_col="go_cmd")
    return dataframe_to_list_table(df, title="常用传送GM命令")
