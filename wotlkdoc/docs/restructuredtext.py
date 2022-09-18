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


def with_columns(
    df: pl.DataFrame,
    named_funcs: T.Dict[str, T.Callable],
) -> pl.DataFrame:
    """
    对 DataFrame 进行处理, 创建新的列, 或者更新已有的列. 更新的逻辑见下

    :param named_funcs: 一个 {key: value} 字典, key 是 column 名字, value 则是一个
        callable function, 这个 function 只接受一个输入, 输入是 DataFrame 的一行,
        而输出可以是任何对象.
    """
    exprs = [
        pl.col(col)
        for col in df.columns
        if col not in named_funcs
    ]
    for col, func in named_funcs.items():
        expr = (
            pl.struct(df.columns)
                .apply(func)
                .alias(col)
        )
        exprs.append(expr)
    return df.select(exprs)


def dataframe_to_list_table(
    df: pl.DataFrame,
    title="",
    **kwargs
) -> ListTable:
    """
    将 DataFrame 转化成 Rst 中的 List Table 对象. 这个 DataFrame 里只允许有

    :param df: DataFrame
    :param title: optional list table title
    :param kwargs: additional keyword argument pass to ``ListTable(**kwargs)``
    """
    lt_data = [list(df.columns), ]
    for row in df.to_dicts():
        lt_data.append(list(row.values()))
    kw = dict(
        data=lt_data,
        title=title,
        index=False,
        header=True,
        class_="sortable",
    )
    kw.update(kwargs)
    lt = ListTable(**kw)
    return lt


def to_add_item_cmd(item_id: T.Union[str, int]) -> CodeBlockPython:
    return convert_to_codeblock_python(f".add {item_id}")


def to_learn_spell_cmd(spell_id: T.Union[str, int]) -> CodeBlockPython:
    return convert_to_codeblock_python(f".learn {spell_id}")


def to_aura_cmd(spell_id: T.Union[str, int]) -> CodeBlockPython:
    return convert_to_codeblock_python(f".aura {spell_id}")


def to_unaura_cmd(spell_id: T.Union[str, int]) -> CodeBlockPython:
    return convert_to_codeblock_python(f".unaura {spell_id}")


def to_modify_rep_cmd(faction_id: T.Union[str, int]) -> CodeBlockPython:
    return convert_to_codeblock_python(f".modify rep {faction_id} 999999")
