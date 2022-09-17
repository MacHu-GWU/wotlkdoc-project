# -*- coding: utf-8 -*-

import polars as pl

from ..importer import (
    TsvGzReader,
    convert_to_codeblock_python,
    dataframe_to_list_table,
)


def lt_popular_mount():
    reader = TsvGzReader(__file__)
    df = reader.read_df("popular-mount.tsv.gz")
    df = df.with_column(pl.col("添加坐骑").apply(f=convert_to_codeblock_python))
    lt = dataframe_to_list_table(
        df,
        title=f"热门坐骑 相关 GM命令",
    )
    return lt


def lt_all_mount():
    reader = TsvGzReader(__file__)
    df = reader.read_df("all-mount.tsv.gz")
    df = df.with_column(pl.col("添加坐骑").apply(f=convert_to_codeblock_python))
    df = df.with_column(pl.col("上马命令").apply(f=convert_to_codeblock_python))
    lt = dataframe_to_list_table(
        df,
        title=f"所有坐骑 相关 GM命令",
    )
    return lt
