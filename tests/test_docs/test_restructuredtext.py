# -*- coding: utf-8 -*-

import os
import pytest
import polars as pl
from wotlkdoc.docs.restructuredtext import (
    convert_to_codeblock_python,
    codify_dataframe,
    dataframe_to_list_table,
)


def test_convert_to_codeblock_python():
    assert convert_to_codeblock_python("line1\nline2").render() == (
        ".. code-block:: python\n"
        "\n"
        "    line1\n"
        "    line2"
    )


def test_codify_dataframe():
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
    new_df = codify_dataframe(
        df,
        {
            column: lambda row: ".add {}".format(row["id"])
        }
    )
    assert new_df["add_item_cmd"][0] == (
        ".. code-block:: python\n"
        "\n"
        "    .add 19019"
    )

    lt = dataframe_to_list_table(new_df, "ItemCode")
    _ = lt.render()


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
