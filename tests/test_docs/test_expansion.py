# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.expansion import lt_expansion


def test():
    lt = lt_expansion()
    lt.render()
    # print(lt.render())


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
