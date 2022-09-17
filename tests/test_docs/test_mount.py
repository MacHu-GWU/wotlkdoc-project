# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.mount import lt_popular_mount, lt_all_mount


def test():
    lt = lt_popular_mount()
    lt.render()
    # print(lt.render())

    lt = lt_all_mount()
    lt.render()
    # print(lt.render())


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
