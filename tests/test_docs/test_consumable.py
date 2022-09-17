# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.consumable import lt_list_consumable


def test():
    for lt, exp, image in lt_list_consumable():
        lt.render()
        # print(lt.render())


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
