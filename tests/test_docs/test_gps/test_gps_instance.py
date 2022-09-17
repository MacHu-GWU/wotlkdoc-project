# -*- coding: utf-8 -*-

import pytest
from wotlkdoc.docs.gps.instance import lt_list_instance_gps


def test():
    lt_list_instance_gps()
    for exp, instance_type, sub_list in lt_list_instance_gps():
        for lt, instance_name, image in sub_list:
            # print(exp, instance_type, instance_name)
            lt.render()
            # print(lt.render())


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
