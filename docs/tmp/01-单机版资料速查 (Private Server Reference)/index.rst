.. _单机版资料速查:

单机版资料速查 (Private Server Reference)
==============================================================================


目录 1
------------------------------------------------------------------------------

.. autotoctree::
    :maxdepth: 1


目录 2
------------------------------------------------------------------------------

.. list-table::
    :widths: 10 10
    :header-rows: 0

    * - 链接
      - 说明
    * - .. image:: /_static/image/portal/13-dalaran.png
            :width: 64px
            :height: 64px
      - :ref:`传送坐标汇总`
    * - .. image:: /_static/image/trade-goods/alchemy/flask.png
            :width: 64px
            :height: 64px
      - :ref:`常用消耗品GM命令`
    * - .. image:: /_static/image/trade-goods/enchanting/enchantment-scroll.png
            :width: 64px
            :height: 64px
      - :ref:`常用附魔物品GM命令`
    * - .. image:: /_static/image//class-icon/01-Warrior.png
            :width: 64px
            :height: 64px
      - :ref:`职业技能代码GM命令`
    * - .. image:: /_static/image/icon/spell_nature_enchantarmor.png
            :width: 64px
            :height: 64px
      - :ref:`天赋技能代码GM命令`
    * - .. image:: /_static/image/icon/ability_warrior_weaponmastery.png
            :width: 64px
            :height: 64px
      - :ref:`学习武器和防具技能的GM命令`
    * - .. image:: /_static/image/trade-skill/enchanting.png
            :width: 64px
            :height: 64px
      - :ref:`学习商业和生活技能的GM命令`
    * - .. image:: /_static/image/icon/achievement_reputation_01.png
            :width: 64px
            :height: 64px
      - :ref:`提高声望的GM命令`
    * - .. image:: /_static/image/mount/ability_mount_ridinghorse.png
            :width: 64px
            :height: 64px
      - :ref:`坐骑相关GM命令`
    * - .. image:: /_static/image/icon/spell_frost_frostbolt02.png
            :width: 64px
            :height: 64px
      - :ref:`装备属性的代码`
    * - .. image:: /_static/image/icon/achievement_pvp_a_14.png
            :width: 64px
            :height: 64px
      - :ref:`PvP物品代码GM命令`
    * - .. image:: /_static/image/icon/temp.png
            :width: 64px
            :height: 64px
      - :ref:`常用代码速查`


魔兽世界服务器和客户端架构简介
------------------------------------------------------------------------------

魔兽世界是典型的客户端和服务端类游戏. 为了提高运算速度, 游戏本地有一份 **静态数据**. 所谓静态数据是指不会随着服务器上的玩家的行为, 以及时间变化而变化的数据. 比如物品 id, 和任务 id, 以及玩家, 物品, 地图, 物品, 人物, 装备 的 2D 或 3D 建模.

而 **服务器** 上主要保存的是玩家的 **状态信息**, 比如每隔一段时间, 或触发相应的事件的话, 就将这些数据写入数据库 (这里只是举例, 更多的数据就不列举了):

1. 玩家角色所在的坐标, 等级, 背包中的物品. 例如, 在获得新物品或是删除物品之后会将改变写入数据库.
2. 玩家学会的技能, 商业技能, 天赋, 成就. 例如, 玩家修改天赋后, 服务器会将改变写入数据库.

而对于 **静态数据** 来说, 服务器上也同样有一份, 为了防止玩家通过修改本地客户端的文件来作弊, 有时候服务器会对其使用 MD5 信息摘要进行验证. 比如物品的实际有效的属性就是由服务器上的物品数据来决定的, 但是物品的显示图标则是由本地客户端上的数据来决定的.
