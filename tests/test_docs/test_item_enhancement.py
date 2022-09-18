# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.item_enhancement import lt_list_item_enhancement


def test():
    for rst_object in lt_list_item_enhancement():
        rst_object.render()
        print(rst_object.render())


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
