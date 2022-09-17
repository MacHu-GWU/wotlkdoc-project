# -*- coding: utf-8 -*-

from . import gps
from .consumable import lt_list_consumable
from .mount import lt_popular_mount, lt_all_mount

doc_data = dict(
    lt_list_common_gps=gps.lt_list_common_gps,
    lt_list_main_city_gps_and_label_and_image=gps.lt_list_main_city_gps_and_label_and_image,
    lt_list_class_trainer_gps=gps.lt_list_class_trainer_gps,
    lt_list_trade_skill_trainer_gps=gps.lt_list_trade_skill_trainer_gps,
    lt_list_east_map_gps=gps.lt_list_east_map_gps,
    lt_list_kali_map_gps=gps.lt_list_kali_map_gps,
    lt_list_tbc_map_gps=gps.lt_list_tbc_map_gps,
    lt_list_wlk_map_gps=gps.lt_list_wlk_map_gps,
    lt_list_instance_gps=gps.lt_list_instance_gps,

    lt_list_consumable=lt_list_consumable,

    lt_popular_mount=lt_popular_mount,
    lt_all_mount=lt_all_mount,
)

# import logging
#
# try:
#     from . import consumable
#     from . import faction
#     from . import mount
#     from . import gps
#     from . import images
#     from ..df_to_list_table import df_to_list_table
#
#     doc_data = dict(
#         # consumable
#         lt_consumable_vanilla=consumable.lt_consumable_vanilla,
#         lt_consumable_tbc=consumable.lt_consumable_tbc,
#         lt_consumable_wlk=consumable.lt_consumable_wlk,
#         rst_list_item_enhancement=consumable.rst_list_item_enhancement,
#
#         lt_faction_vanilla=faction.lt_faction_vanilla,
#         lt_faction_tbc=faction.lt_faction_tbc,
#         lt_faction_wlk=faction.lt_faction_wlk,
#         lt_mount=mount.lt_mount,
#
#         # gps zone
#         lt_list_east_map_gps=gps.lt_list_east_map_gps,
#         lt_list_kali_map_gps=gps.lt_list_kali_map_gps,
#         lt_list_tbc_map_gps=gps.lt_list_tbc_map_gps,
#         lt_list_wlk_map_gps=gps.lt_list_wlk_map_gps,
#
#         # gps city
#         lt_list_main_city_gps=gps.lt_list_main_city_gps,
#
#         # gps class trainer
#         lt_list_class_trainer_gps=gps.lt_list_class_trainer_gps,
#
#         # gps trade skill trainer
#         lt_list_trade_skill_trainer_gps=gps.lt_list_trade_skill_trainer_gps,
#
#         # gps instance, dungeon, raid
#         list_of_lt_list_instance_gps=gps.list_of_lt_list_instance_gps,
#
#         func_df_to_list_table=df_to_list_table,
#
#         # image links
#         # maps
#         img_map_tbc=images.img_map_tbc,
#         img_map_wlk=images.img_map_wlk,
#         img_map_cities=images.img_map_cities,
#     )
# except Exception as e:
#     logging.warning(str(e))
