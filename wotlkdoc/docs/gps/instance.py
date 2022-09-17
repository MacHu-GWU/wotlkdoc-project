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


def lt_list_instance_gps() -> T.List[
    T.Tuple[
        str, # expansion
        str, # instance_type
        T.List[
            T.Tuple[
                "ListTable",
                str, # instance_name,
                "Image",
            ]
        ]
    ]
]:
    reader = TsvGzReader(__file__)
    df = reader.read_df("instance.tsv.gz")
    df = (
        df.select(
            [
                pl.col("exp").alias("资料片"),
                pl.col("instance_type").alias("副本类型"),
                pl.col("name").alias("副本"),
                pl.col("loc").alias("地点"),
                pl.col("go_cmd").alias("go_cmd"),
            ]
        )
            .fill_null("")
            .filter(pl.col("go_cmd") != "")
    )
    df = with_teleport_command(df, go_cmd_col="go_cmd")
    lst = list()
    for exp in df["资料片"].unique(maintain_order=True):
        sub_df = df.filter(df["资料片"] == exp)
        for instance_type in sub_df["副本类型"].unique(maintain_order=True):
            sub_sub_df = sub_df.filter(sub_df["副本类型"] == instance_type)

            sub_lst = list()
            for instance_name in sub_sub_df["副本"].unique(maintain_order=True):
                sub_sub_sub_df = sub_sub_df.filter(sub_sub_df["副本"] == instance_name)
                image = image_by_map(instance_name)
                image.height = 480
                sub_lst.append(
                    (
                        dataframe_to_list_table(
                            sub_sub_sub_df.drop(["资料片", "副本类型"]),
                            title=f"{instance_name} 传送GM命令",
                        ),
                        instance_name,
                        image,
                    )
                )
            lst.append((exp, instance_type, sub_lst))
    return lst
