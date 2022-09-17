# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.gps.class_skill_trainer import lt_list_class_trainer_gps


def test():
    lt = lt_list_class_trainer_gps()
    lt.render()
    # print(lt.render())


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
