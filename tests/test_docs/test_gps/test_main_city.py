# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.gps.main_city import lt_list_main_city_gps_and_label_and_image


def test():
    lst = lt_list_main_city_gps_and_label_and_image()
    for lt, city, image in lst:
        lt.render()
        # print(lt.render())


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
