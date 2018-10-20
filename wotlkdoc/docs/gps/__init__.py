# -*- coding: utf-8 -*-

from pypinyin import pinyin, Style
from rstobj.directives import ListTable

try:
    from ... import utils
except:
    from wotlkdoc import utils

reader = utils.CurrentDirDataFrameReader(__file__)

chinese_columns = "exp,land,area,faction,category,name".split(",")
lt_columns_en = "exp,land,area,faction,category,name".split(",")
lt_columns_cn = "资料片,大陆,地图,阵营,类别,名称,传送命令1,传送命令2".split(",")
df_city = reader.read_csv("city.tsv")
# lt_city = df_city[]


exp_list = ["经典旧世", "燃烧的远征", "巫妖王之怒"]
section_name_list = ["各大地图", "五人小队副本", "团队副本"]

lt_快速索引_data = []
快速索引_链接模板 = ":ref:`{exp} <{exp}{section_name}传送>`"
for exp in exp_list:
    row = list()
    row.append(快速索引_链接模板.format(exp=exp, section_name=""))
    for section_name in section_name_list:
        row.append(快速索引_链接模板.format(exp=exp, section_name=section_name))
    lt_快速索引_data.append(row)
lt_快速索引_data.append([
    "各大主城", "职业技能训练师", "商业技能训练师",
])

lt_快速索引 = ListTable(
    data=lt_快速索引_data,
    title="快速索引", index=False, header=False,
)

# ltable = ListTable(
#     data=
# )
#
# ngram_columns = list()

# for chn_c in chinese_columns:
#     ngram_columns.append(chn_c)
#
#     new_c = chn_c + "_pinyin"
#     ngram_columns.append(new_c)
#     df[new_c] = df[chn_c].apply(utils.get_pinyin)
#
#     new_c = chn_c + "_pinyin_initial"
#     ngram_columns.append(new_c)
#     df[new_c] = df[chn_c].apply(utils.get_first_letter_pinyin)
#
# df.to_json("gps.json", orient="records", force_ascii=False)
# print(ngram_columns)
