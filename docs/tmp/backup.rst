.. _传送坐标汇总:

传送坐标汇总 (Teleport)
==============================================================================

.. contents:: 目录
    :depth: 1
    :local:

.. image:: /_static/images/expansion-logo/WoW01-Vanilla-Logo.png
    :height: 64 px
.. image:: /_static/images/expansion-logo/WoW02-The-Burning-Crusade-Logo.png
    :height: 64 px
.. image:: /_static/images/expansion-logo/WoW03-Wrath-of-the-Lich-King-Logo.png
    :height: 64 px

.. jinja:: doc_data
    {{ doc_data.lt_vanilla_east_gps.render() }}

.. jinja:: doc_data

    {{ doc_data.lt_vanilla_kalimdor_gps.render() }}

.. jinja:: doc_data

    {{ doc_data.lt_tbc_map_gps.render() }}


.. _巫妖王之怒地图传送GM命令:

巫妖王之怒 地图传送GM命令
------------------------------------------------------------------------------

.. contents:: 目录
    :local:

.. jinja:: doc_data

    {% for map, df in doc_data.df_list_wlk_map_gps %}
    {{ map }}
    ~~~~~~~~~~~~~~~~~~~~
    .. image:: {{ doc_data.map_wlk[map] }}
        :height: 480

    {{ doc_data.func_df_to_list_table(df, title=" 传送GM命令".format(map), code_column_and_transform_func={"传送命令1": None, "传送命令2": None}).render() }}
    {% endfor %}



主城 传送GM命令
------------------------------------------------------------------------------

.. contents:: 目录
    :local:

.. jinja:: doc_data

    {% for city, df_city_gps in doc_data.df_list_main_city_gps %}
    {{ city }}
    ~~~~~~~~~~~~~~~~~~~~
    .. image:: {{ doc_data.map_cities[city] }}
        :height: 480

    {{ doc_data.func_df_to_list_table(df_city_gps, title=" 传送GM命令".format(city), code_column_and_transform_func={"传送命令1": None, "传送命令2": None}).render() }}
    {% endfor %}
