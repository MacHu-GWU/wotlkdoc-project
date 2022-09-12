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

    columns = "城市,地点,描述,go_cmd".split(",")
    df.columns = columns
    df1 = with_teleport_command(df, go_cmd_col="go_cmd")
    df2 = df1.with_column(pl.col("城市").apply(f=icon_by_portal).alias("图标"))
    df3 = df2.select("图标,城市,地点,描述,传送命令1,传送命令2".split(","))

    lst = list()
    for city in df3["城市"].unique(maintain_order=True):
        sub_df = df3.filter(df3["城市"] == city)
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
