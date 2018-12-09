# -*- coding: utf-8 -*-

"""
This module helps transform pandas.DataFrame to Restructured Text List Table.
It allows user to embed code block in the table.
"""

from rstobj.directives import ListTable, CodeBlockBase, CodeBlockPython, Code


def convert_to_codeblock_python(value):
    """
    将字符串转化为 CodeBlockPython 对象
    :param value:
    :return:
    """
    try:
        if isinstance(value, CodeBlockBase):
            return value
        else:
            return CodeBlockPython(code=Code(text="%s" % value))
    except:
        return value


def df_to_list_table(df, title="", code_column_and_transform_func=None):
    """
    将 DataFrame 转化成 Rst 中的 List Table 对象.

    :param df: DataFrame
    :param title: Title
    :param code_column_and_transform_func:
        - key: column name
        - value: None, or a simple text transform function,
            should take a row as the single argument
    :return:
    """
    if code_column_and_transform_func is None:
        code_column_and_transform_func = dict()

    for col, func in code_column_and_transform_func.items():
        if func is None:
            func = lambda row: row[col]

        transform_func = lambda row: convert_to_codeblock_python(func(row))

        if col in df.columns:
            df.loc[df.index, col] = df.apply(transform_func, axis=1)

    lt_data = [list(df.columns), ]
    lt_data.extend(df.to_records(index=False))

    lt = ListTable(
        data=lt_data, title=title, index=False, header=True, class_="sortable"
    )
    return lt


if __name__ == "__main__":
    import pandas as pd

    df = pd.DataFrame(
        [
            ("雷霆之怒, 逐风者的祝福之剑", 19019),
            ("埃辛诺斯战刃, 主手", 32837),
            ("埃辛诺斯战刃, 副手", 32838),
            ("影之哀伤", 49623)
        ],
        columns=["name", "id"]
    )
    df.rename(columns={"id": "add_item_cmd"}, inplace=True)
    lt = df_to_list_table(
        df=df,
        title="item",
        code_column_and_transform_func={
            "add_item_cmd": lambda row: ".add %s" % row["add_item_cmd"],
            # "add_item_cmd": None,
        }
    )
    print(lt.render())
