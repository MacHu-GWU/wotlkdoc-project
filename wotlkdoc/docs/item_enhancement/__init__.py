# -*- coding: utf-8 -*-

import typing as T
import polars as pl
from rstobj import Header, TableOfContent, ListTable

from ..importer import (
    TsvGzReader,
    dataframe_to_list_table,
    to_add_item_cmd,
)


def lt_list_item_enhancement() -> T.List[T.Union[Header, TableOfContent, ListTable]]:
    reader = TsvGzReader(__file__)
    df = reader.read_df("item-enhancement.tsv.gz")
    wanted_columns = "名称,描述,附魔部位,GM命令".split(",")
    df = (
        df
            .filter(
            pl.col("物品等级") >= 50
        )
            .with_column(
            pl.col("物品ID").apply(f=to_add_item_cmd).alias("GM命令"),
        )
    )
    lst = list()
    toc = TableOfContent(
        depth=1,
        local=True,
        class_="this-will-duplicate-information-and-it-is-still-useful-here",
    )

    # 附魔卷轴速查, 先按照 资料片 排序, 然后按照 部位 排序
    lst.append(
        Header(
            title="附魔卷轴GM命令速查",
            ref_label="附魔卷轴GM命令速查",
            header_level=3,
            bar_length=79,
        )
    )
    lst.append(toc)
    df1 = df.filter(pl.col("来源") == "附魔")
    for exp in df1["资料片"].unique(maintain_order=True):
        sub_df = df1.filter(pl.col("资料片") == exp)
        lst.append(Header(title=exp, header_level=4, bar_length=79))
        lst.append(toc)
        for slot in sub_df["附魔部位"].unique(maintain_order=True):
            sub_sub_df = sub_df.filter(pl.col("附魔部位") == slot)
            lst.append(Header(title=slot, header_level=5, bar_length=79))
            lst.append(toc)
            lst.append(
                dataframe_to_list_table(
                    sub_sub_df.select(wanted_columns),
                    title=f"{exp} {slot} 部位附魔卷轴",
                )
            )

    # 裁缝, 制皮, 锻造 附魔物品
    profession_list = ["裁缝", "制皮", "锻造"]
    for profession in profession_list:
        title = f"{profession}附魔物品GM命令速查"
        lst.append(Header(title=title, ref_label=title, header_level=3, bar_length=79))
        lst.append(toc)
        sub_df = df.filter(pl.col("来源") == profession)
        lst.append(
            dataframe_to_list_table(
                sub_df.select(wanted_columns),
                title=f"{profession} 附魔物品",
            )
        )

    # 特殊附魔物品速查, 按照 资料片 排序
    lst.append(
        Header(
            title="特殊附魔物品GM命令速查",
            ref_label="特殊附魔物品GM命令速查",
            header_level=3,
            bar_length=79,
        )
    )
    lst.append(toc)
    df1 = df.filter(pl.col("来源").is_in("声望,荣誉,副本".split(",")))
    for exp in df1["资料片"].unique(maintain_order=True):
        sub_df = df1.filter(pl.col("资料片") == exp)
        lst.append(Header(title=exp, header_level=4, bar_length=79))
        lst.append(
            dataframe_to_list_table(
                sub_df.select(wanted_columns),
                title=f"{exp} 特殊附魔",
            )
        )

    return lst