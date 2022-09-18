# -*- coding: utf-8 -*-

import typing as T
import polars as pl

from ..importer import (
    TsvGzReader,
    dataframe_to_list_table,
    to_modify_rep_cmd,
)
from ..images import image_by_exp

if T.TYPE_CHECKING:
    from rstobj import Image, ListTable


def lt_list_faction() -> T.List[
    T.Tuple['ListTable', str, 'Image']
]:
    reader = TsvGzReader(__file__)
    df = reader.read_df("faction.tsv.gz")
    df = df.select([
        pl.col("expansion").alias("资料片"),
        pl.col("type").alias("类型"),
        pl.col("name").alias("阵营"),
        pl.col("reward").alias("奖励"),
        pl.col("faction_id").alias("编号"),
        pl.col("faction_id").apply(f=to_modify_rep_cmd).alias("崇拜命令"),
    ])
    lst = list()
    for exp in df["资料片"].unique(maintain_order=True):
        sub_df = df.filter(df["资料片"] == exp).drop("资料片")
        image = image_by_exp(exp)
        lst.append(
            (
                dataframe_to_list_table(sub_df, title=f"{exp}声望崇拜GM命令"),
                exp,
                image,
            )
        )
    return lst
