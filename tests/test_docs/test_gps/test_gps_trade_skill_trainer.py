# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.gps.trade_skill_trainer import lt_list_trade_skill_trainer_gps


def test():
    lst = lt_list_trade_skill_trainer_gps()
    for lt, trade_skill, image in lst:
        lt.render()
        # print(lt.render())
        break


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
