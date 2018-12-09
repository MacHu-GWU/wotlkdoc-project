# -*- coding: utf-8 -*-

from .helper import (
    remove_go_cmd_construct_teleport,
    disaggregate_df_transform_to_list_table,
)
from ...compressed_tsv import make_gzip, read_compressed_tsv

make_gzip(this_file=__file__, filename="main-city.tsv")
df_main_city_gps = read_compressed_tsv(this_file=__file__, filename="main-city.tsv.gz")
df_main_city_gps.columns = "城市,地点,描述,gm_cmd".split(",")
df_main_city_gps = remove_go_cmd_construct_teleport(df_main_city_gps)
lt_list_main_city_gps = disaggregate_df_transform_to_list_table(df_main_city_gps, "城市")

if __name__ == "__main__":
    print(lt_list_main_city_gps[0][1].render())
