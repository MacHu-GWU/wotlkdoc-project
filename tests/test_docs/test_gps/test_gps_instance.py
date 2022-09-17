# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.gps.instance import lt_list_instance_gps


def test():
    lt_list_instance_gps()
    # for exp, instance_type, sub_list in lt_list_instance_gps():
    #     print(exp, instance_type)
    # for lst in [
    #     lt_list_east_map_gps(),
    #     lt_list_kali_map_gps(),
    #     lt_list_tbc_map_gps(),
    #     lt_list_wlk_map_gps(),
    # ]:
    #     for lt, map, image in lst:
    #         lt.render()
    #         print(lt.render())
    #         break
    pass


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
