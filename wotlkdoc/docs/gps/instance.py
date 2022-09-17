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




# instance_gps_columns = "资料片,副本类型,名称,位置,gm_cmd".split(",")
#
# tsv_filename = "instance.tsv"
# make_gzip(this_file=__file__, filename=tsv_filename)
# df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
# df.columns = instance_gps_columns
#
# exp_order = dict(
#     经典旧世=1,
#     燃烧的远征=2,
#     巫妖王之怒=3,
# )
# instance_type_order = dict(
#     小队副本=1,
#     团队副本=2,
# )
#
# list_of_lt_list_instance_gps = list()
# """
# list_of_lt_list_instance_gps = [
#     (exp, instance_type, lt_list),
#     ...
# ]
#
# lt_list = [
#     (name, list_table),
#     ...
# ]
# """
#
# for exp, sub_df in sorted(df.groupby("资料片"), key=lambda x: exp_order[x[0]]):
#     for instance_type, sub_sub_df in sorted(sub_df.groupby("副本类型"), key=lambda x: instance_type_order[x[0]]):
#         sub_sub_df = sub_sub_df["名称,位置,gm_cmd".split(",")].copy()
#         sub_sub_df = remove_go_cmd_construct_teleport(sub_sub_df)
#         lt_list = disaggregate_df_transform_to_list_table(sub_sub_df, "名称")
#         list_of_lt_list_instance_gps.append((exp, instance_type, lt_list))
#
# if __name__ == "__main__":
#     assert len(list_of_lt_list_instance_gps) == 6
#
#     for exp, instance_type, lt_list in list_of_lt_list_instance_gps:
#         for name, lt in lt_list:
#             print(lt.render())
#             break
#         break
