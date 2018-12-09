# -*- coding: utf-8 -*-

from rstobj.directives.codeblock import CodeBlockPython, Code
from .gps_cmd import parse_go_command, construct_go_command, is_valid_go_command
from ...df_to_list_table import df_to_list_table


def remove_go_cmd_construct_teleport(df, gm_cmd_col="gm_cmd"):
    """
    :param gm_cmd_col: the .go GM command column name.

    **中文文档**

    从 ``gm_cmd`` 列导出 ``传送命令1`` 和 ``传送命令2`` 列中的数据, 并删除 ``gm_cmd``.
    传送命令列中的对象是一个 :class:`CodeBlockPython` 对象.
    """
    gm_cmd_list = list()
    for v in df[gm_cmd_col]:
        v = v.strip()
        if is_valid_go_command(v):
            gm_cmd_list.append(construct_go_command(*parse_go_command(v)))
        else:
            print("`{}` is not a valid .go command".format(v))
            gm_cmd_list.append(v)
    df[gm_cmd_col] = gm_cmd_list

    df["传送命令1"] = df[gm_cmd_col].apply(
        lambda v: CodeBlockPython(code=Code(text=v))
    )
    df["传送命令2"] = df[gm_cmd_col].apply(
        lambda v: CodeBlockPython(code=Code(text=v.replace(".go", ".go xyz")))
    )
    df.drop(columns=[gm_cmd_col], inplace=True)
    return df


def disaggregate_df_transform_to_list_table(df, column):
    """
    Transform::

        cate    value
        a       1
        a       2
        b       3
        b       4

    To::

        [("a", df1), ("b", df2)]

    df1::

        cate    value
        a       1
        a       2

    df2::

        cate    value
        b       3
        b       4
    """
    return [
        (label, df_to_list_table(df[df[column] == label].copy(), title="{}传送GM命令".format(label)))
        for label in df[column].unique()
    ]
