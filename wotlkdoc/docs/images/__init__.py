# -*- coding: utf-8 -*-

import typing as T
from collections import Counter
from pathlib_mate import Path
from rstobj import Image
from ..paths import dir_source, dir_static


def image_path_to_href(img_path: str):
    """
    Assuming ``dir_static = "/home/username/wotlkdoc-project/docs/source/_static``,
    given an file path of an image that in the ``_static`` folder   ``/home/username/wotlkdoc-project/docs/source/_static/wotlkdoc-logo.png``,
    return the url href link ``/_static/wotlkdoc-logo.png``, which can be used
    in restructuredtext ``image`` directive.
    """
    rel_path = Path(img_path).relative_to(dir_source)
    return "/" + str(rel_path)


def image_path_to_rst_obj(
    img_path: str,
    height: int = None,
    width: int = None,
    scale: int = None,
    alt_text: str = None,
    align: str = None,
) -> Image:
    return Image(
        uri=image_path_to_href(img_path),
        height=height,
        width=width,
        scale=scale,
        alt_text=alt_text,
        align=align,
    )


dir_image = dir_static / "image"

dir_class_icon = dir_image / "class-icon"

_class_icon_mapper = dict(
    战士="01-Warrior.png",
    圣骑士="02-Paladin.png",
    死亡骑士="03-DeathKnight.png",
    死骑="03-DeathKnight.png",
    猎人="04-Hunter.png",
    萨满="05-Shaman.png",
    盗贼="06-Rogue.png",
    德鲁伊="07-Druid.png",
    法师="08-Mage.png",
    术士="09-Warlock.png",
    牧师="10-Priest.png",
    全部="All.png",
    warrior="01-Warrior.png",
    paladin="02-Paladin.png",
    deathknight="03-DeathKnight.png",
    dk="03-DeathKnight.png",
    hunter="04-Hunter.png",
    shaman="05-Shaman.png",
    rogue="06-Rogue.png",
    druid="07-Druid.png",
    mage="08-Mage.png",
    warlock="09-Warlock.png",
    priest="10-Priest.png",
    all="All.png",
)


def image_by_class(class_: str) -> Image:
    img_path = dir_class_icon / _class_icon_mapper[class_.lower()]
    return image_path_to_rst_obj(img_path=img_path, height=64)


dir_trade_skill_icon = dir_image / "trade-skill"

_trade_skill_icon_mapper = dict(
    炼金="alchemy.png",
    锻造="blacksmithing.png",
    烹饪="cooking.png",
    附魔="enchanting.png",
    工程学="engineering.png",
    急救="first-aid.png",
    钓鱼="fishing.png",
    采药="herbalism.png",
    铭文="inscription.png",
    珠宝加工="jewelcrafting.png",
    制皮="leatherworking.png",
    采矿="mining.png",
    剥皮="skinning.png",
    裁缝="tailoring.png",
    全部="all.png",
    alchemy="alchemy.png",
    blacksmithing="blacksmithing.png",
    cooking="cooking.png",
    enchanting="enchanting.png",
    engineering="engineering.png",
    first_aid="first-aid.png",
    fishing="fishing.png",
    herbalism="herbalism.png",
    inscription="inscription.png",
    jewelcrafting="jewelcrafting.png",
    leatherworking="leatherworking.png",
    mining="mining.png",
    skinning="skinning.png",
    tailoring="tailoring.png",
    all="all.png",
)


def image_by_trade_skill(trade_skill: str) -> Image:
    img_path = dir_trade_skill_icon / _trade_skill_icon_mapper[trade_skill.lower()]
    return image_path_to_rst_obj(img_path=img_path, height=64)


dir_faction_icon = dir_image / "faction-icon"

_faction_icon_mapper = dict(
    联盟="alliance.png",
    人类="human.png",
    矮人="dwarf.png",
    侏儒="gnome.png",
    暗夜精灵="nightelf.png",
    德莱尼="draenei.png",
    部落="horde.png",
    兽人="orc.png",
    巨魔="troll.png",
    牛头人="tauren.png",
    亡灵="undead.png",
    血精灵="bloodelf.png",
    中立="neutral.png",
    alliance="alliance.png",
    human="human.png",
    dwarf="dwarf.png",
    gnome="gnome.png",
    nightelf="nightelf.png",
    draenei="draenei.png",
    horde="horde.png",
    orc="orc.png",
    troll="troll.png",
    tauren="tauren.png",
    undead="undead.png",
    bloodelf="bloodelf.png",
    neutral="neutral.png",
)


def image_by_faction(faction: str) -> Image:
    img_path = dir_faction_icon / _faction_icon_mapper[faction.lower()]
    return image_path_to_rst_obj(img_path=img_path, height=64)


dir_portal_icon = dir_image / "portal"

_portal_icon_mapper = dict(
    暴风城="01-stormwind.png",
    铁炉堡="02-ironforge.png",
    达纳苏斯="03-darnassus.png",
    埃索达="04-exodar.png",
    塞拉摩="05-theramore.png",
    奥格瑞玛="06-orgrimmar.png",
    雷霆崖="07-thunderbluff.png",
    幽暗城="08-undercity.png",
    银月城="09-silvermoon.png",
    斯通纳德="10-stonard.png",
    月光林地="11-moonglade.png",
    沙塔斯城="12-shattrath.png",
    达拉然="13-dalaran.png",
    黯黑堡="14-ebonhold.png",
    stormwind="01-stormwind.png",
    ironforge="02-ironforge.png",
    darnassus="03-darnassus.png",
    exodar="04-exodar.png",
    theramore="05-theramore.png",
    orgrimmar="06-orgrimmar.png",
    thunderbluff="07-thunderbluff.png",
    undercity="08-undercity.png",
    silvermoon="09-silvermoon.png",
    stonard="10-stonard.png",
    moonglade="11-moonglade.png",
    shattrath="12-shattrath.png",
    dalaran="13-dalaran.png",
    ebonhold="14-ebonhold.png",
)


def icon_by_portal(portal: str) -> Image:
    img_path = dir_portal_icon / _portal_icon_mapper[portal.lower()]
    return image_path_to_rst_obj(img_path=img_path, height=64)


dir_map = dir_image / "map"

_pairs = [
    (p.fname, p)
    for p in dir_map.select_image()
]

_counter = Counter([
    fname
    for fname, _ in _pairs
])

for key, count in _counter.items():
    if count > 1:
        raise ValueError(
            f"please fix your image file name, "
            f"found duplicate file name: {key!r}"
        )

map_image_mapper = {
    fname: p
    for fname, p in _pairs
}

# add some alias
# Vanilla
map_image_mapper["血色修道院"] = map_image_mapper["血色修道院-教堂"]
map_image_mapper["厄运之槌"] = map_image_mapper["厄运之槌-入口"]
map_image_mapper["通灵学院"] = map_image_mapper["通灵学院1"]
map_image_mapper["斯坦索姆"] = map_image_mapper["斯坦索姆1"]
map_image_mapper["黑石塔"] = map_image_mapper["黑石山-入口"]
map_image_mapper["黑石塔上层"] = map_image_mapper["黑石山-黑石塔上层"]
map_image_mapper["黑石塔下层"] = map_image_mapper["黑石山-黑石塔下层1"]
map_image_mapper["熔火之心"] = map_image_mapper["黑石山-熔火之心"]
map_image_mapper["黑翼之巢"] = map_image_mapper["黑石山-黑翼之巢"]
map_image_mapper["安其拉废墟"] = map_image_mapper["安其拉-安其拉废墟"]
map_image_mapper["安其拉神殿"] = map_image_mapper["安其拉-安其拉神殿"]

# TBC
map_image_mapper["地狱火城墙"] = map_image_mapper["地狱火堡垒-地狱火城墙"]
map_image_mapper["鲜血熔炉"] = map_image_mapper["地狱火堡垒-鲜血熔炉"]
map_image_mapper["破碎大厅"] = map_image_mapper["地狱火堡垒-破碎大厅"]

map_image_mapper["奴隶围栏"] = map_image_mapper["盘牙水库-奴隶围栏"]
map_image_mapper["幽暗沼泽"] = map_image_mapper["盘牙水库-幽暗沼泽"]
map_image_mapper["蒸汽地窟"] = map_image_mapper["盘牙水库-蒸汽地窟"]

map_image_mapper["法力陵墓"] = map_image_mapper["奥金顿-法力陵墓"]
map_image_mapper["奥金尼地穴"] = map_image_mapper["奥金顿-奥金尼地穴"]
map_image_mapper["赛泰克大厅"] = map_image_mapper["奥金顿-赛泰克大厅"]
map_image_mapper["暗影迷宫"] = map_image_mapper["奥金顿-暗影迷宫"]

map_image_mapper["旧希尔斯布莱德丘陵"] = map_image_mapper["时光之穴-旧希尔斯布莱德丘陵1"]
map_image_mapper["黑色沼泽"] = map_image_mapper["时光之穴-黑色沼泽"]

map_image_mapper["能源舰"] = map_image_mapper["风暴要塞-能源舰"]
map_image_mapper["生态船"] = map_image_mapper["风暴要塞-生态船"]
map_image_mapper["禁魔监狱"] = map_image_mapper["风暴要塞-禁魔监狱"]

map_image_mapper["玛瑟里顿的巢穴"] = map_image_mapper["地狱火堡垒-玛瑟里顿的巢穴"]
map_image_mapper["卡拉赞"] = map_image_mapper["卡拉赞-入口"]
map_image_mapper["祖阿曼"] = map_image_mapper["祖阿曼1"]
map_image_mapper["毒蛇神殿"] = map_image_mapper["盘牙水库-毒蛇神殿"]
map_image_mapper["风暴要塞"] = map_image_mapper["风暴要塞-风暴要塞"]
map_image_mapper["海加尔峰"] = map_image_mapper["时光之穴-海加尔峰"]
map_image_mapper["黑暗神殿"] = map_image_mapper["黑暗神殿-起始"]

# WLK
map_image_mapper["岩石大厅"] = map_image_mapper["奥杜尔-岩石大厅"]
map_image_mapper["闪电大厅"] = map_image_mapper["奥杜尔-闪电大厅"]
map_image_mapper["纳克萨玛斯"] = map_image_mapper["纳克萨玛斯1"]
map_image_mapper["奥杜尔"] = map_image_mapper["奥杜尔-城墙"]
map_image_mapper["冠军的试炼"] = map_image_mapper["十字军大竞技场-冠军的试炼"]
map_image_mapper["十字军的试炼"] = map_image_mapper["十字军大竞技场-十字军的试炼"]
map_image_mapper["映像大厅"] = map_image_mapper["冰封大厅-映像大厅"]
map_image_mapper["灵魂洪炉"] = map_image_mapper["冰封大厅-灵魂洪炉"]
map_image_mapper["萨隆矿坑"] = map_image_mapper["冰封大厅-萨隆矿坑"]
map_image_mapper["冰冠堡垒"] = map_image_mapper["冰冠堡垒-冰封王座"]


def image_by_map(map_name: str) -> Image:
    img_path = map_image_mapper[map_name]
    return image_path_to_rst_obj(img_path=img_path)
