# -*- coding: utf-8 -*-

import os
import pytest

from wotlkdoc.docs.gps.go_cmd import GoCmd


class TestGoCmd:
    def test_from_string(self):
        go_cmd = GoCmd.from_string("123.123 456.456 789.789 0")
        assert go_cmd.go_cmd == ".go 123.12 456.46 789.79 0"

        go_cmd = GoCmd.from_string(".go 123.123 456.456 789.789 0")
        assert go_cmd.go_cmd == ".go 123.12 456.46 789.79 0"

        go_cmd = GoCmd.from_string(".go xyz 123.123 456.456 789.789 0")
        assert go_cmd.go_cmd == ".go 123.12 456.46 789.79 0"


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
