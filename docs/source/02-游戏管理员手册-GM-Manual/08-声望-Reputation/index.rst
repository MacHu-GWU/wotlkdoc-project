.. _提高声望的GM命令:

提高声望的GM命令 (Faction)
===============================================================================

.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

.. image:: Reputation.png

------

.. image:: /_static/image/expansion-logo/WoW01-Vanilla-Logo.png
    :target: 经典旧世声望GM命令_
    :height: 64 px

.. image:: /_static/image/expansion-logo/WoW02-The-Burning-Crusade-Logo.png
    :target: 燃烧的远征声望GM命令_
    :height: 64 px

.. image:: /_static/image/expansion-logo/WoW03-Wrath-of-the-Lich-King-Logo.png
    :target: 巫妖王之怒声望GM命令_
    :height: 64 px

本文档列出了 **巫妖王之怒** 版本中所有牵涉到的声望列表. 如果你想要修改某个声望到崇拜 (或任意等级), 而你又知道 Faction Id, 则可以使用以下命令:

    .modify rep faction_id value

关于如何查找 Faction Id, 和声望在单机版服务端中的详细信息, 请参考 :ref:`what-is-faction`.

关于官方魔兽世界中 **声望** 的相关支持, 可以参考 :ref:`WIKI-声望`.


.. _经典旧世声望代码:

经典旧世声望
------------------------------------------------------------------------------
经典旧世声望的正常冲法请参考 :ref:`Vanilla-Faction`

.. note::

    **下面所有的文本都可以被一键拷贝到宏命令中, 实现批量修改**


联盟主城与战场
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 72 999999
            .modify rep 47 999999
            .modify rep 69 999999
            .modify rep 54 999999

            .modify rep 890 999999
            .modify rep 509 999999
            .modify rep 730 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 72 999999 暴风城
            .modify rep 47 999999 铁炉堡
            .modify rep 69 999999 达纳苏斯
            .modify rep 54 999999 诺莫瑞根流亡者

            .modify rep 890 999999 银翼要塞 战歌峡谷
            .modify rep 509 999999 阿拉索联军 阿拉希高地
            .modify rep 730 999999 雷矛卫队 奥特兰克山谷
            /targetlasttarget


部落主城与战场
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 76 999999
            .modify rep 68 999999
            .modify rep 81 999999
            .modify rep 530 999999

            .modify rep 889 999999
            .modify rep 510 999999
            .modify rep 729 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 76 999999 奥格瑞玛
            .modify rep 68 999999 幽暗城
            .modify rep 81 999999 雷霆崖
            .modify rep 530 999999 暗矛巨魔

            .modify rep 889 999999 战歌先遣队 战歌峡谷
            .modify rep 510 999999 污染者 阿拉希高地
            .modify rep 729 999999 霜狼氏族 奥特兰克山谷
            /targetlasttarget


热砂港集团, 四大地精城市
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 21 999999
            .modify rep 577 999999
            .modify rep 470 999999
            .modify rep 369 999999
            .modify rep 169 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 21 999999 藏宝海湾
            .modify rep 577 999999 永望镇
            .modify rep 470 999999 棘齿城
            .modify rep 369 999999 加基森
            .modify rep 169 999999 热砂港
            /targetlasttarget


团队副本相关或奖励丰厚的声望
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 576 999999
            .modify rep 529 999999
            .modify rep 59 999999
            .modify rep 749 999999
            .modify rep 270 999999
            .modify rep 609 999999
            .modify rep 910 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 576 999999 木喉要塞
            .modify rep 529 999999 银色黎明
            .modify rep 59 999999 瑟银兄弟会
            .modify rep 749 999999 海达希亚水元素
            .modify rep 270 999999 赞达拉部族
            .modify rep 609 999999 塞纳里奥议会
            .modify rep 910 999999 诺斯多姆的子嗣
            /targetlasttarget


其他
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 809 999999
            .modify rep 87 999999
            .modify rep 349 999999
            .modify rep 909 999999
            .modify rep 589 999999
            .modify rep 92 999999
            .modify rep 93 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 809 999999 辛德拉
            .modify rep 87 999999 血帆海盗
            .modify rep 349 999999 拉文霍德
            .modify rep 909 999999 暗月马戏团
            .modify rep 589 999999 冬刃豹训练师
            .modify rep 92 999999 吉尔吉斯半人马
            .modify rep 93 999999 玛格拉姆半人马
            /targetlasttarget


.. _燃烧的远征声望代码:

燃烧的远征声望
------------------------------------------------------------------------------
燃烧的远征声望的正常冲法请参考 :ref:`TBC-Faction`


主城
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 930 999999
            .modify rep 911 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 930 999999 埃索达
            .modify rep 911 999999 银月城
            /targetlasttarget


附魔
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 头部附魔
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 946 999999
            .modify rep 947 999999
            .modify rep 942 999999
            .modify rep 1011 999999
            .modify rep 935 999999
            .modify rep 989 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 946 999999 荣耀堡 治疗附魔
            .modify rep 947 999999 萨尔玛 治疗附魔
            .modify rep 942 999999 塞纳里奥远征队 物理DPS附魔
            .modify rep 1011 999999 贫民窟 魔战士附魔
            .modify rep 935 999999 沙塔尔 法系DPS附魔
            .modify rep 989 999999 时光守护者 坦克附魔
            /targetlasttarget

.. list-table:: 肩部附魔
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 932 999999
            .modify rep 934 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 932 999999 奥多尔 肩膀附魔
            .modify rep 934 999999 占星者 肩膀附魔
            /targetlasttarget


团队副本
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 967 999999
            .modify rep 990 999999
            .modify rep 1012 999999
            .modify rep 1077 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 967 999999 紫罗兰之眼 卡拉赞声望戒指
            .modify rep 990 999999 流沙之鳞 海加尔山声望戒指
            .modify rep 1012 999999 灰舌死誓者 黑暗神庙声望饰品
            .modify rep 1077 999999 破碎残阳 黑暗神殿珠宝配方
            /targetlasttarget


坐骑
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 1031 999999
            .modify rep 1015 999999
            .modify rep 978 999999
            .modify rep 941 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 1031 999999 沙塔尔天空卫队 虚空鳐坐骑
            .modify rep 1015 999999 虚空之翼 灵翼游龙坐骑
            .modify rep 978 999999 库雷尼 联盟塔布羊坐骑
            .modify rep 941 999999 玛格哈 部落塔布羊坐骑
            /targetlasttarget


其他
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 933 999999
            .modify rep 970 999999

            .modify rep 936 999999
            .modify rep 1050 999999
            .modify rep 922 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 933 999999 星界财团 珠宝专业
            .modify rep 970 999999 孢子村 特殊配方和饰品

            .modify rep 936 999999 沙塔尔所有声望
            .modify rep 1050 999999 奥格瑞拉 剑刃山脉挖水晶
            .modify rep 922 999999 塔奎林 幽魂之地
            /targetlasttarget


.. _巫妖王之怒WLK声望代码:

巫妖王之怒WLK声望
------------------------------------------------------------------------------
巫妖王之怒声望的正常冲法请参考 :ref:`WLK-Faction`


附魔和ICC戒指 (必冲)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 1119 999999
            .modify rep 1090 999999
            .modify rep 1091 999999
            .modify rep 1098 999999
            .modify rep 1106 999999
            .modify rep 1156 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 1119 999999 霍迪尔之子 全职业肩膀附魔
            .modify rep 1090 999999 肯瑞托 法系DPS附魔
            .modify rep 1091 999999 龙眠联军 治疗附魔
            .modify rep 1098 999999 黑锋骑士团 物理DPS附魔
            .modify rep 1106 999999 银色北伐军 坦克附魔
            .modify rep 1156 999999 灰烬审判军 ICC声望戒指
            /targetlasttarget


联盟军队
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 1037 999999
            .modify rep 1050 999999
            .modify rep 1068 999999
            .modify rep 1126 999999
            .modify rep 1094 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 1037 999999 联盟先遣军 PvP附魔
            .modify rep 1050 999999 无畏远征军
            .modify rep 1068 999999 探险者协会
            .modify rep 1126 999999 霜脉矮人
            .modify rep 1094 999999 银色盟约 联盟角鹰兽飞行坐骑
            /targetlasttarget


部落军队
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 1052 999999
            .modify rep 1064 999999
            .modify rep 1067 999999
            .modify rep 1085 999999
            .modify rep 1124 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 1052 999999 部落先遣军 PvP附魔
            .modify rep 1064 999999 牦牛人
            .modify rep 1067 999999 复仇之手
            .modify rep 1085 999999 战歌远征军
            .modify rep 1124 999999 夺日者 部落龙鹰飞行坐骑
            /targetlasttarget


其他
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 声望崇拜命令
      - 说明
    * - ::

            /target player
            .modify rep 1073 999999
            .modify rep 1104 999999
            .modify rep 1105 999999
            /targetlasttarget

      - ::

            /target player
            .modify rep 1073 999999 卡鲁亚克 海象人钓鱼竿
            .modify rep 1104 999999 狂心部族
            .modify rep 1105 999999 神谕者
            /targetlasttarget


.. _声望ID速查:

附录: 声望ID速查
------------------------------------------------------------------------------

.. jinja:: doc_data

    {% for lt, exp, image in doc_data.lt_list_faction() %}
    {{ exp }}声望GM命令
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    {{ image.render() }}

    {{ lt.render() }}
    {% endfor %}
