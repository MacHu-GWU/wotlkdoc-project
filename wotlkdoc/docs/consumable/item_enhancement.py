# -*- coding: utf-8 -*-

"""

**中文文档**:

常用附魔物品速查表.
"""

from wotlkdoc.compressed_tsv import make_gzip, read_compressed_tsv
from wotlkdoc.df_to_list_table import df_to_list_table
from rstobj.directives import CodeBlockPython, Code, TableOfContent
from rstobj.markup import Header

# 附魔卷轴速查, 按照 资料片,  然后按照 部位
toc_depth1_local = TableOfContent(depth=1, local=True)

rst_list_item_enhancement = list()
rst_list_item_enhancement.append(
    Header(title="附魔卷轴速查", ref_label="附魔卷轴GM命令速查", header_level=2)
)
rst_list_item_enhancement.append(toc_depth1_local)

tsv_filename = "item-enhancement.tsv"
make_gzip(this_file=__file__, filename=tsv_filename)
df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
df["GM命令"] = df["物品ID"].apply(lambda v: CodeBlockPython(code=Code(text=".add %s" % v)))

useful_columns = "名称,描述,附魔部位,GM命令".split(",")
df_enchanting = df[(df["来源"] == "附魔") & (df["物品等级"] >= 50)]
for exp, sub_df1 in df_enchanting.groupby("资料片"):
    rst_list_item_enhancement.append(Header(title=exp, header_level=3))
    rst_list_item_enhancement.append(toc_depth1_local)
    for place, sub_df2 in sub_df1.groupby("附魔部位"):
        sub_df2 = sub_df2.sort_values("物品等级", ascending=False)
        sub_df2 = sub_df2[useful_columns].copy()
        rst_list_item_enhancement.append(Header(title=place, header_level=4))

        title = "{exp} 附魔卷轴".format(exp=exp, place=place)
        lt = df_to_list_table(sub_df2, title=title, code_column_and_transform_func={"GM命令": None})
        rst_list_item_enhancement.append(lt)

# 裁缝, 制皮, 锻造 附魔
profession_list = ["裁缝", "制皮", "锻造"]
for profession in profession_list:
    title = "{profession}附魔物品".format(profession=profession)
    rst_list_item_enhancement.append(Header(title=title, header_level=2))
    sub_df = df[(df["来源"] == profession)]
    sub_df = sub_df[useful_columns].copy()
    lt = df_to_list_table(sub_df, title=title, code_column_and_transform_func={"GM命令": None})
    rst_list_item_enhancement.append(lt)


# 特殊附魔物品速查, 按照在资料片
rst_list_item_enhancement.append(
    Header(title="特殊附魔物品速查", ref_label="特殊附魔物品GM命令速查", header_level=2)
)
rst_list_item_enhancement.append(toc_depth1_local)

useful_columns = "名称,描述,具体来源,特殊需求,附魔部位,GM命令".split(",")
df_special_enchanting = df[df["来源"].isin("声望,荣誉,副本".split(","))]
for exp, sub_df in df_special_enchanting.groupby("资料片"):
    rst_list_item_enhancement.append(Header(title=exp, header_level=3))

    title = "{exp} 特殊附魔".format(exp=exp)
    sub_df = sub_df[useful_columns].copy()
    lt = df_to_list_table(
        sub_df, title=title, code_column_and_transform_func={"GM命令": None}
    )
    rst_list_item_enhancement.append(lt)


# rst_list_item_enhancement = "\n".join([
#     item.render(bar_length=78)
#     for item in rst_list_item_enhancement
# ])
# print(rst_list_item_enhancement)
# if __name__ == "__main__":
#     for item in rst_list_item_enhancement:
#         print(item.render(bar_length=80))