# -*- coding: utf-8 -*-

import typing as T
import polars as pl

from ..importer import (
    TsvGzReader,
    dataframe_to_list_table,
)
from ..images import icon_by_portal, image_by_map
from .go_cmd import with_teleport_command

if T.TYPE_CHECKING:
    from rstobj import Image, ListTable


def lt_list_main_city_gps_and_label_and_image() -> T.List[
    T.Tuple['ListTable', str, 'Image']
]:
    reader = TsvGzReader(__file__)
    df = reader.read_df("main-city.tsv.gz")
    df = df.select([
        pl.col("zone").alias("城市"),
        pl.col("zone").alias("图标"),
        pl.col("loc_name").alias("地点"),
        pl.col("description").alias("描述"),
        pl.col("go_cmd").alias("go_cmd"),
    ])
    df1 = with_teleport_command(df, go_cmd_col="go_cmd")
    df2 = df1.with_column(pl.col("图标").apply(f=icon_by_portal))
    lst = list()
    for city in df2["城市"].unique(maintain_order=True):
        sub_df = df2.filter(df2["城市"] == city)
        image = image_by_map(city)
        image.height = 480
        lst.append(
            (
                dataframe_to_list_table(sub_df, title=f"{city}传送GM命令"),
                city,
                image,
            )
        )
    return lst
