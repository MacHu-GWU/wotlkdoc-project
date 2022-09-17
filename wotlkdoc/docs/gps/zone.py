# -*- coding: utf-8 -*-

import typing as T
import polars as pl

from ..importer import (
    TsvGzReader,
    dataframe_to_list_table,
)
from ..images import image_by_map
from .go_cmd import with_teleport_command

if T.TYPE_CHECKING:
    from rstobj import Image, ListTable


def _lt_list_zone_gps_and_label_and_image(
    filename: str,
) -> T.List[T.Tuple["ListTable", str, "Image"]]:
    reader = TsvGzReader(__file__)
    df = reader.read_df(filename)
    df = (
        df.select(
            [
                pl.col("zone").alias("地图"),
                pl.col("loc").alias("地点"),
                pl.col("detail").alias("位置"),
                pl.col("description").alias("描述"),
                pl.col("go_cmd").alias("go_cmd"),
            ]
        )
            .fill_null("")
            .filter(pl.col("go_cmd") != "")
    )
    df = with_teleport_command(df, go_cmd_col="go_cmd")
    lst = list()
    for map in df["地图"].unique(maintain_order=True):
        sub_df = df.filter(df["地图"] == map)
        image = image_by_map(map)
        image.height = 480
        lst.append(
            (
                dataframe_to_list_table(
                    sub_df,
                    title=f"{map} 传送GM命令",
                ),
                map,
                image,
            )
        )
    return lst


def lt_list_east_map_gps():
    return _lt_list_zone_gps_and_label_and_image("zone-1-a-vanilla-eastern-kingdom.tsv")


def lt_list_kali_map_gps():
    return _lt_list_zone_gps_and_label_and_image("zone-1-b-vanilla-kalimdor.tsv.gz")


def lt_list_tbc_map_gps():
    return _lt_list_zone_gps_and_label_and_image("zone-2-tbc.tsv.gz")


def lt_list_wlk_map_gps():
    return _lt_list_zone_gps_and_label_and_image("zone-3-wlk.tsv.gz")
