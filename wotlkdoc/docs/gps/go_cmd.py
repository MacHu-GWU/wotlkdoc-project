# -*- coding: utf-8 -*-

"""
Parse and format ``.go x y z`` command.
"""

import attr
from attrs_mate import AttrsClass
import polars as pl
from ..restructuredtext import convert_to_codeblock_python, with_columns


@attr.s
class GoCmd(AttrsClass):
    """
    Represent a GM ``.go x y z`` command.
    """
    x: float = attr.ib()
    y: float = attr.ib()
    z: float = attr.ib()
    map_id: int = attr.ib()

    @property
    def go_cmd(self) -> str:
        return ".go {:.1f} {:.1f} {:.1f} {}".format(
            self.x,
            self.y,
            self.z,
            self.map_id,
        )

    @property
    def go_xyz_cmd(self) -> str:
        return ".go xyz {:.1f} {:.1f} {:.1f} {}".format(
            self.x,
            self.y,
            self.z,
            self.map_id,
        )

    @classmethod
    def from_string(cls, s: str) -> 'GoCmd':
        """
        Valid format:

        - "1.23 4.56 7.89 0"
        - ".go 1.23 4.56 7.89 0"
        - ".go xyz 1.23 4.56 7.89 0"
        """
        s = s.strip()
        if s.startswith(".go"):
            if "xyz" in s:
                _, _, x, y, z, map_id = s.split(" ")
            else:
                _, x, y, z, map_id = s.split(" ")
        else:
            x, y, z, map_id = s.split(" ")
        return GoCmd(
            x=float(x),
            y=float(y),
            z=float(z),
            map_id=int(map_id),
        )


def with_teleport_command(
    df: pl.DataFrame,
    go_cmd_col: str = "go_cmd",
):
    """
    :param df: 一个 DataFrame, 必须有一列是包含 .go x y z 命令
    :param go_cmd_col: 原始 .go x y z 命令所在的列名

    例如, 输入如果是::

        go_cmd
        .go 111 222 333 0

    那么 "go_cmd" 列将会被替换成 "传送命令1" 和 "传送命令2" 两列, 原来的 "go_cmd" 将会被
    删除, 返回的输出是::

        传送命令1                       传送命令2
        .. code-block:: python         .. code-block:: python

            .go 111 222 333 0               .go xyz 111 222 333 0
    """
    return with_columns(
        df,
        named_funcs={
            "传送命令": lambda row: convert_to_codeblock_python(GoCmd.from_string(row[go_cmd_col]).go_xyz_cmd),
        }
    ).drop(go_cmd_col)
