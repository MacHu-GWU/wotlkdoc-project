# -*- coding: utf-8 -*-

import os
import pytest
from wotlkdoc.docs.images import (
    image_path_to_href,
    image_path_to_rst_obj,
    dir_source,
    image_by_class,
    image_by_trade_skill,
    image_by_map,
)


def test_image_path_to_href_and_image_path_to_rst_obj():
    img_path = (dir_source / "_static" / "wotlkdoc-logo.png").abspath
    assert image_path_to_href(img_path) == "/_static/wotlkdoc-logo.png"
    assert image_path_to_rst_obj(img_path).uri == "/_static/wotlkdoc-logo.png"


def test_image_by_class():
    assert image_by_class("战士").uri == "/_static/image/class-icon/01-Warrior.png"
    assert image_by_class("DK").uri == "/_static/image/class-icon/03-DeathKnight.png"
    assert image_by_class("全部").uri == "/_static/image/class-icon/All.png"


def test_image_by_trade_skill():
    assert image_by_trade_skill("锻造").uri == "/_static/image/trade-skill/blacksmithing.png"
    assert image_by_trade_skill("blacksmithing").uri == "/_static/image/trade-skill/blacksmithing.png"
    

def test_image_by_map():
    assert image_by_map("暴风城").uri == "/_static/image/map/03-主城/暴风城.jpg"
    assert image_by_map("东瘟疫之地").uri == "/_static/image/map/11-东部王国/东瘟疫之地.jpg"
    assert image_by_map("贫瘠之地").uri == "/_static/image/map/12-卡利姆多/贫瘠之地.jpg"
    assert image_by_map("地狱火半岛").uri == "/_static/image/map/21-外域/地狱火半岛.jpg"
    assert image_by_map("冰冠冰川").uri == "/_static/image/map/31-北裂境/冰冠冰川.jpg"


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
