.. _传送坐标汇总:

传送坐标汇总 (Teleport)
==============================================================================
.. contents:: 目录
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


.. list-table:: **快速索引**
    :widths: 10 10 10 10 10
    :header-rows: 0

    * - 资料片
      - 地图传送
      - 地图传送
      - 小队副本
      - 团队副本
    * - .. image:: /_static/image/expansion-logo/WoW01-Vanilla-Logo.png
            :height: 64px
      - .. image:: /_static/image/icon/achievement_zone_easternkingdoms_01.png
            :width: 64px
            :height: 64px
            :target: 东部王国地图传送GM命令_
      - .. image:: /_static/image/icon/achievement_zone_kalimdor_01.png
            :width: 64px
            :height: 64px
            :target: 卡利姆多地图传送GM命令_
      - .. image:: /_static/image/icon/achievement_dungeon_classicdungeonmaster.png
            :width: 64px
            :height: 64px
            :target: 经典旧世-小队副本-传送GM命令_
            :alt: 经典旧世 小队副本 传送GM命令
      - .. image:: /_static/image/icon/achievement_dungeon_classicraider.png
            :width: 64px
            :height: 64px
            :target: 经典旧世-团队副本-传送GM命令_
    * - .. image:: /_static/image/expansion-logo/WoW02-The-Burning-Crusade-Logo.png
            :height: 64px
      - .. image:: /_static/image/icon/achievement_zone_outland_01.png
            :width: 64px
            :height: 64px
            :target: 燃烧的远征地图传送GM命令_
      -
      - .. image:: /_static/image/icon/achievement_dungeon_classicdungeonmaster.png
            :width: 64px
            :height: 64px
            :target: 燃烧的远征-小队副本-传送GM命令_
      - .. image:: /_static/image/icon/achievement_dungeon_classicraider.png
            :width: 64px
            :height: 64px
            :target: 燃烧的远征-团队副本-传送GM命令_
    * - .. image:: /_static/image/expansion-logo/WoW03-Wrath-of-the-Lich-King-Logo.png
            :height: 64px
      - .. image:: /_static/image/icon/achievement_zone_northrend_01.png
            :width: 64px
            :height: 64px
            :target: 巫妖王之怒地图传送GM命令_
      -
      - .. image:: /_static/image/icon/achievement_dungeon_classicdungeonmaster.png
            :width: 64px
            :height: 64px
            :target: 巫妖王之怒-小队副本-传送GM命令_
      - .. image:: /_static/image/icon/achievement_dungeon_classicraider.png
            :width: 64px
            :height: 64px
            :target: 巫妖王之怒-团队副本-传送GM命令_


.. _常用传送GM命令:

常用传送GM命令
------------------------------------------------------------------------------
.. jinja:: doc_data

    {{ doc_data.lt_list_common_gsp().render() }}


.. _主城传送GM命令:

主城 传送 GM命令
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


.. jinja:: doc_data

    {% for lt, city, image in doc_data.lt_list_main_city_gps_and_label_and_image() %}
    {{ city }}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    {{ image.render() }}

    {{ lt.render() }}
    {% endfor %}


.. _职业技能训练师传送GM命令:

职业技能训练师 传送 GM命令
------------------------------------------------------------------------------
.. jinja:: doc_data

    {{ doc_data.lt_list_class_trainer_gsp().render() }}


.. _商业技能训练师传送GM命令:

商业技能训练师 传送GM命令
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

.. jinja:: doc_data

    {% for lt, trade_skill, image in doc_data.lt_list_trade_skill_trainer_gsp() %}
    .. _{{ trade_skill }}训练师传送GM命令:

    {{ trade_skill }} 训练师传送GM命令
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    {{ image.render() }}

    {{ lt.render() }}
    {% endfor %}


.. _东部王国地图传送GM命令:

东部王国 传送GM命令
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

.. jinja:: doc_data

    {% for lt, map, image in doc_data.lt_list_east_map_gps() %}
    {{ map }}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    {{ image.render() }}

    {{ lt.render() }}
    {% endfor %}


.. _卡利姆多地图传送GM命令:

卡利姆多 地图 传送GM命令
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

.. jinja:: doc_data

    {% for lt, map, image in doc_data.lt_list_kali_map_gps() %}
    {{ map }}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    {{ image.render() }}

    {{ lt.render() }}
    {% endfor %}


.. _燃烧的远征地图传送GM命令:

燃烧的远征 地图 传送GM命令
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

.. jinja:: doc_data

    {% for lt, map, image in doc_data.lt_list_tbc_map_gps() %}
    {{ map }}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    {{ image.render() }}

    {{ lt.render() }}
    {% endfor %}


.. _巫妖王之怒地图传送GM命令:

巫妖王之怒 地图 传送GM命令
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

.. jinja:: doc_data

    {% for lt, map, image in doc_data.lt_list_wlk_map_gps() %}
    {{ map }}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    {{ image.render() }}

    {{ lt.render() }}
    {% endfor %}


.. _副本传送GM命令:

副本 传送GM命令
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


.. jinja:: doc_data

    {% for exp, instance_type, sub_lst in doc_data.lt_list_instance_gps() %}

    .. _{{ exp }}-{{ instance_type }}-传送GM命令:

    {{ exp }} {{ instance_type }} 传送GM命令
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    .. contents::
        :class: this-will-duplicate-information-and-it-is-still-useful-here
        :depth: 1
        :local:

    {% for lt, instance_name, image in sub_lst %}
    .. _{{ instance_name }}-传送GM命令:

    {{ instance_name }}
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    {{ image.render() }}

    {{ lt.render() }}
    {% endfor %}
    {% endfor %}
