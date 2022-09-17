# -*- coding: utf-8 -*-

import os
import pytest
import polars as pl

from wotlkdoc.docs.gps.go_cmd import GoCmd, with_teleport_command


class TestGoCmd:
    def test_from_string(self):
        go_cmd = GoCmd.from_string("123.123 456.456 789.789 0")
        assert go_cmd.go_cmd == ".go 123.1 456.5 789.8 0"

        go_cmd = GoCmd.from_string(".go 123.123 456.456 789.789 0")
        assert go_cmd.go_cmd == ".go 123.1 456.5 789.8 0"

        go_cmd = GoCmd.from_string(".go xyz 123.123 456.456 789.789 0")
        assert go_cmd.go_cmd == ".go 123.1 456.5 789.8 0"


def test_with_teleport_command():
    data = [
        (".go 123.12 456.46 789.79 0",),
    ]
    df = pl.DataFrame(data, columns=["go_command", ])
    new_df = with_teleport_command(df, go_cmd_col="go_command")
    assert new_df.columns == ["传送命令", ]


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
