# -*- coding: utf-8 -*-

import typing as T
import polars as pl

from ..importer import (
    TsvGzReader,
    dataframe_to_list_table,
)
from ..images import image_by_trade_skill
from .go_cmd import with_teleport_command

if T.TYPE_CHECKING:
    from rstobj import Image, ListTable


def lt_list_trade_skill_trainer_gsp() -> T.List[T.Tuple["ListTable", str, "Image"]]:
    reader = TsvGzReader(__file__)
    df = reader.read_df("trade-skill-trainer.tsv.gz")

    df = df.select([
        pl.col("faction").alias("阵营"),
        pl.col("category").alias("商业技能"),
        pl.col("sub_category").alias("等级范围"),
        pl.col("loc").alias("位置"),
        pl.col("go_cmd"),
    ])
    df = with_teleport_command(df, go_cmd_col="go_cmd")

    lst = list()
    for trade_skill in df["商业技能"].unique(maintain_order=True):
        sub_df = df.filter(df["商业技能"] == trade_skill)
        sub_df = sub_df.drop("商业技能")
        image = image_by_trade_skill(trade_skill)
        lst.append(
            (
                dataframe_to_list_table(
                    sub_df,
                    title=f"{trade_skill} 传送GM命令",
                ),
                trade_skill,
                image,
            )
        )
    return lst
