# -*- coding: utf-8 -*-

import os
import pytest
import polars as pl

from rstobj import CodeBlockPython
from wotlkdoc.docs.restructuredtext import (
    convert_to_codeblock_python,
    with_columns,
    dataframe_to_list_table,
)


def test_convert_to_codeblock_python():
    assert convert_to_codeblock_python("line1\nline2").render() == (
        ".. code-block:: python\n"
        "\n"
        "    line1\n"
        "    line2"
    )


def test_with_columns():
    df = pl.DataFrame(
        [
            ("雷霆之怒, 逐风者的祝福之剑", 19019),
            ("埃辛诺斯战刃, 主手", 32837),
            ("埃辛诺斯战刃, 副手", 32838),
            ("影之哀伤", 49623)
        ],
        columns=["name", "id"]
    )
    column = "add_item_cmd"
    new_df = with_columns(
        df,
        {
            column: lambda row: convert_to_codeblock_python(".add {}".format(row["id"]))
        }
    )
    assert isinstance(new_df.to_dicts()[0][column], CodeBlockPython)


def test_dataframe_to_list_table():
    df = pl.DataFrame(
        [
            [123, ],
            [456, ],
        ],
        columns=["id", ]
    )
    new_df = with_columns(
        df,
        {
            "add_item": lambda row: convert_to_codeblock_python(".add {}".format(row["id"]))
        }
    )
    lt = dataframe_to_list_table(new_df, title="Add Item")
    print([lt.render(), ])
    assert lt.render() == (
        ".. list-table:: Add Item\n"
        "    :class: sortable\n"
        "    :header-rows: 1\n"
        "    :stub-columns: 0\n"
        "\n"
        "    * - id\n"
        "      - add_item\n"
        "    * - 123\n"
        "      - .. code-block:: python\n"
        "        \n"
        "            .add 123\n"
        "    * - 456\n"
        "      - .. code-block:: python\n"
        "        \n"
        "            .add 456\n"
    )


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
