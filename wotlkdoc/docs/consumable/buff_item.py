# -*- coding: utf-8 -*-

from wotlkdoc.compressed_tsv import make_gzip, read_compressed_tsv
from wotlkdoc.df_to_list_table import df_to_list_table

tsv_filename = "buff-item.tsv"
make_gzip(this_file=__file__, filename=tsv_filename)
df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
df.columns = (
    "资料片,类型,效果类型,名称,效果,添加物品命令"
).split(",")


def construct_list_table(expansion):
    return df_to_list_table(
        df=df[df["资料片"] == expansion].copy().drop(columns=["资料片", ]),
        title="{}合剂, 药剂, 药水, 食物和饮料".format(expansion),
        code_column_and_transform_func={
            "添加物品命令": lambda row: ".add {id} -20\n.add {id} 20 # {name}".format(id=row["添加物品命令"], name=row["名称"])
        },
    )


lt_consumable_vanilla = construct_list_table("经典旧世")
lt_consumable_tbc = construct_list_table("燃烧的远征")
lt_consumable_wlk = construct_list_table("巫妖王之怒")

if __name__ == "__main__":
    print(lt_consumable_vanilla.render())
