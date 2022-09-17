# -*- coding: utf-8 -*-

import polars as pl

from ..importer import (
    TsvGzReader,
    to_add_item_cmd,
    dataframe_to_list_table,
)
from ..images import image_by_exp


def lt_list_consumable():
    reader = TsvGzReader(__file__)
    df = reader.read_df("consumable.tsv.gz")
    df = df.select([
        pl.col("expansion").alias("资料片"),
        pl.col("type").alias("类型"),
        pl.col("name").alias("名称"),
        pl.col("effect").alias("效果"),
        pl.col("item_id"),
    ])

    df = df.with_column(pl.col("item_id").apply(f=to_add_item_cmd).alias("添加物品命令"))

    lst = list()
    for exp in df["资料片"].unique(maintain_order=True):
        sub_df = df.filter(df["资料片"] == exp).drop(["资料片"])
        image = image_by_exp(exp)
        lst.append(
            (
                dataframe_to_list_table(
                    sub_df,
                    title=f"{exp} 常用消耗品GM命令",
                ),
                exp,
                image,
            )
        )
    return lst
