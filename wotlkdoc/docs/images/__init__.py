# -*- coding: utf-8 -*-

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
    img_path = dir_class_icon / _class_icon_mapper[class_]
    return image_path_to_rst_obj(img_path=img_path)


dir_map = dir_image / "map"
dir_main_city = dir_map / "03-主城"

def image_by_main_city(main_city: str) -> Image:
    img_path = dir_main_city / f"{main_city}.jpg"
    return image_path_to_rst_obj(img_path=img_path)

# dir_eastern_kingdom =  dir_map / "11-东部王国"
# dir_kalimdor =  dir_map / "11-东部王国"
# dir_outland =  dir_map / "21-外域"
# dir_northrend =  dir_map / "31-北裂境"


def image_by_map(map_name: str) -> Image:
    pass
img_map_tbc = dict(
    地狱火半岛="https://i.imgur.com/MueAcLX.jpg",
    赞加沼泽="https://i.imgur.com/xpciIKj.jpg",
    泰罗卡森林="https://i.imgur.com/JRnJlIW.jpg",
    纳格兰="https://i.imgur.com/GppbuCB.jpg",
    刀锋山="https://i.imgur.com/jEMq31v.jpg",
    虚空风暴="https://i.imgur.com/WDtzOef.jpg",
    影月谷="https://i.imgur.com/UtHI1Gy.jpg",
    沙塔斯城="https://i.imgur.com/NO134U7.jpg",
)

img_map_wlk = dict(
    北风苔原="https://i.imgur.com/h9QlUoU.jpg",
    嚎风峡湾="https://i.imgur.com/wOZ1Zn6.jpg",
    龙骨荒野="https://i.imgur.com/o0vGdFo.jpg",
    灰熊丘陵="https://i.imgur.com/0pR1d4G.jpg",
    祖达克="https://i.imgur.com/cHrLJrV.jpg",
    索拉查盆地="https://i.imgur.com/VmsyACr.jpg",
    风暴峭壁="https://i.imgur.com/veq31Yk.jpg",
    冰冠冰川="https://i.imgur.com/PABhFc7.jpg",
    洛斯加尔登陆点="https://i.imgur.com/sEfpaxF.jpg",
    冬拥湖="https://i.imgur.com/a50CVD6.jpg",
    晶歌森林="https://i.imgur.com/cdWXFgV.jpg",
    达拉然="https://i.imgur.com/bH5O89K.jpg"
)

img_class_icon = dict(
    战士="/_static/image/class-icon/01-Warrior.png",
    圣骑士="/_static/image/class-icon/02-Paladin.png",
    死亡骑士="/_static/image/class-icon/03-DeathKnight.png",
    猎人="/_static/image/class-icon/04-Hunter.png",
    萨满="/_static/image/class-icon/05-Shaman.png",
    盗贼="/_static/image/class-icon/06-Rogue.png",
    德鲁伊="/_static/image/class-icon/07-Druid.png",
    法师="/_static/image/class-icon/08-Mage.png",
    术士="/_static/image/class-icon/09-Warlock.png",
    牧师="/_static/image/class-icon/10-Priest.png",
    全部="/_static/image/class-icon/All.png",
)

img_trade_skill = dict(
    炼金="/_static/image/trade-skill/alchemy.png",
    锻造="/_static/image/trade-skill/blacksmithing.png",
    烹饪="/_static/image/trade-skill/cooking.png",
    附魔="/_static/image/trade-skill/enchanting.png",
    工程学="/_static/image/trade-skill/engineering.png",
    急救="/_static/image/trade-skill/first-aid.png",
    钓鱼="/_static/image/trade-skill/fishing.png",
    采药="/_static/image/trade-skill/herbalism.png",
    铭文="/_static/image/trade-skill/inscription.png",
    珠宝加工="/_static/image/trade-skill/jewelcrafting.png",
    制皮="/_static/image/trade-skill/leatherworking.png",
    采矿="/_static/image/trade-skill/mining.png",
    剥皮="/_static/image/trade-skill/skinning.png",
    裁缝="/_static/image/trade-skill/tailoring.png",
)
