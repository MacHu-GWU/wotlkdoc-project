# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.gps.common import lt_list_common_gps


def test():
    lt = lt_list_common_gps()
    lt.render()
    # print(lt.render())


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
