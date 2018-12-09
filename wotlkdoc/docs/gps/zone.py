# -*- coding: utf-8 -*-

"""

"""
try:
    from .helper import (
        remove_go_cmd_construct_teleport,
        disaggregate_df_transform_to_list_table,
    )
except:
    from wotlkdoc.docs.gps.helper import (
        remove_go_cmd_construct_teleport,
        disaggregate_df_transform_to_list_table,
    )
from wotlkdoc.compressed_tsv import make_gzip, read_compressed_tsv

zone_gps_columns = "地图,地点,位置,描述,gm_cmd".split(",")
"""
各个地图的 GM 传送命令一定都有这么5列.
"""


def read_data_and_derive_df_list(tsv_filename):
    make_gzip(this_file=__file__, filename=tsv_filename)
    df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
    df.columns = zone_gps_columns
    df = remove_go_cmd_construct_teleport(df)
    lt_list = disaggregate_df_transform_to_list_table(df, "地图")
    return lt_list


lt_list_east_map_gps = read_data_and_derive_df_list("vanilla-eastern-kingdom-gps.tsv")
lt_list_kali_map_gps = read_data_and_derive_df_list("vanilla-kalimdor-gps.tsv")
lt_list_tbc_map_gps = read_data_and_derive_df_list("tbc-map-gps.tsv")
lt_list_wlk_map_gps = read_data_and_derive_df_list("wlk-map-gps.tsv")

if __name__ == "__main__":
    print(lt_list_east_map_gps[0][1].render())
