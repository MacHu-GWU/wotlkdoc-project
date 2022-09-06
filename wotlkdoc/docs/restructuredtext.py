# -*- coding: utf-8 -*-

"""
该模块的目的是从数据中生成 Restructured Text 代码.
"""

import typing as T

import polars as pl
from rstobj.directives import ListTable, CodeBlockPython, Code


def convert_to_codeblock_python(value: T.Union[str, int]) -> CodeBlockPython:
    """
    将字符串转化为 ``CodeBlockPython`` 对象.
    """
    return CodeBlockPython(code=Code(text="%s" % value))


def codify_dataframe(
    df: pl.DataFrame,
    col_and_func: T.Dict[str, T.Callable] = None,
) -> pl.DataFrame:
    records = list()
    for record in df.to_dicts():
        for col, func in col_and_func.items():
            value = convert_to_codeblock_python(func(record)).render()
            record[col] = value
        records.append(record)
    new_df = pl.DataFrame(records)
    return new_df


def dataframe_to_list_table(
    df: pl.DataFrame,
    title="",
):
    """
    将 DataFrame 转化成 Rst 中的 List Table 对象.

    :param df: DataFrame
    :param title: optional list table title
    """
    lt_data = [list(df.columns), ]
    for row in df.to_dicts():
        lt_data.append(list(row.values()))
    lt = ListTable(
        data=lt_data,
        title=title,
        index=False,
        header=True,
        class_="sortable",
    )
    return lt
