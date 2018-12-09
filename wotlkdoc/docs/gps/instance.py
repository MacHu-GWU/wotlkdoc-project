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

instance_gps_columns = "资料片,副本类型,名称,位置,gm_cmd".split(",")

tsv_filename = "instance.tsv"
make_gzip(this_file=__file__, filename=tsv_filename)
df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
df.columns = instance_gps_columns

exp_order = dict(
    经典旧世=1,
    燃烧的远征=2,
    巫妖王之怒=3,
)
instance_type_order = dict(
    小队副本=1,
    团队副本=2,
)

list_of_lt_list_instance_gps = list()
"""
list_of_lt_list_instance_gps = [
    (exp, instance_type, lt_list),
    ...
]

lt_list = [
    (name, list_table),
    ...
]
"""

for exp, sub_df in sorted(df.groupby("资料片"), key=lambda x: exp_order[x[0]]):
    for instance_type, sub_sub_df in sorted(sub_df.groupby("副本类型"), key=lambda x: instance_type_order[x[0]]):
        sub_sub_df = sub_sub_df["名称,位置,gm_cmd".split(",")].copy()
        sub_sub_df = remove_go_cmd_construct_teleport(sub_sub_df)
        lt_list = disaggregate_df_transform_to_list_table(sub_sub_df, "名称")
        list_of_lt_list_instance_gps.append((exp, instance_type, lt_list))

if __name__ == "__main__":
    assert len(list_of_lt_list_instance_gps) == 6

    for exp, instance_type, lt_list in list_of_lt_list_instance_gps:
        for name, lt in lt_list:
            print(lt.render())
            break
        break
