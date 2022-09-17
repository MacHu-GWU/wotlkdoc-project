# -*- coding: utf-8 -*-

import polars as pl

from ..importer import (
    TsvGzReader,
    dataframe_to_list_table,
)
from ..images import image_by_trade_skill
from .go_cmd import with_teleport_command


def lt_list_trade_skill_trainer_gsp():
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
    df = df.with_column(pl.col("商业技能").apply(f=image_by_trade_skill))

    return dataframe_to_list_table(df, title="商业技能训练师传送GM命令")





# def read_data_and_derive_df_list(tsv_filename):
#     make_gzip(this_file=__file__, filename=tsv_filename)
#     df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
#     df.columns = trade_skill_trainer_gps_columns
#     df = remove_go_cmd_construct_teleport(df)
#
#     def construct_img(trade_skill_name):
#         if trade_skill_name in img_trade_skill:
#             return Image(uri=img_trade_skill[trade_skill_name], width=64, height=64)
#         else:
#             return trade_skill_name
#
#     label_column = "商业技能"
#     df_list = [
#         [label, df[df[label_column] == label].copy()]
#         for label in df[label_column].unique()
#     ]
#     for pair in df_list:
#         trade_skill_name = pair[0]
#         sub_df = pair[1]
#         sub_df[label_column] = sub_df[label_column].apply(construct_img)
#         pair[1] = df_to_list_table(sub_df, title="{}".format(trade_skill_name))
#
#     lt_list = df_list
#     return lt_list
#
#
# lt_list_trade_skill_trainer_gsp = read_data_and_derive_df_list("trade-skill-trainer.tsv")
#
# if __name__ == "__main__":
#     print(lt_list_trade_skill_trainer_gsp[0][1].render())
