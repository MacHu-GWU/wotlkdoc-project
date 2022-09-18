# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.faction import lt_list_faction


def test():
    for i in lt_list_faction():
        # lt.render()
        # print(lt.render())
        pass


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
