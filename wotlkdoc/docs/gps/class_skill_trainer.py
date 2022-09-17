# -*- coding: utf-8 -*-

import polars as pl

from ..importer import (
    TsvGzReader,
    dataframe_to_list_table,
)
from ..images import image_by_class, image_by_faction
from .go_cmd import with_teleport_command


def lt_list_class_trainer_gsp():
    reader = TsvGzReader(__file__)
    df = reader.read_df("class-skill-trainer.tsv.gz")
    df = df.select([
        pl.col("faction").alias("阵营"),
        pl.col("class").alias("职业"),
        pl.col("city").alias("城市"),
        pl.col("loc").alias("位置"),
        pl.col("go_cmd"),
    ])
    df1 = with_teleport_command(df, go_cmd_col="go_cmd")

    df2 = df1.with_column(pl.col("阵营").apply(f=image_by_faction))
    df3 = df2.with_column(pl.col("职业").apply(f=image_by_class))

    return dataframe_to_list_table(df3, title="职业技能训练师传送GM命令")
