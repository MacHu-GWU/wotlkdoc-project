.. _常用附魔物品GM命令:

常用附魔物品 (Item Enhancement)
==============================================================================
.. image:: /_static/image/trade-skill/enchanting.png
.. image:: /_static/image/trade-goods/enchanting/enchantment-scroll.png


各资料片, 各职业定位的各部位附魔物品的GM命令速查
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


巫妖王之怒
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

因为同一类职业定位各个部位所需要的最强附魔大致上是相同的, 例如 ``法系DPS`` 定位包含了 所有专精的 ``法师``, ``术士`` 以及 ``暗牧``. 所以我们可以 **用一个宏命令获得某个职业定位的所有附魔**.

非锻造职业可以使用锻造的制品 ``永恒腰带扣``, 为自己的腰带添加一个珠宝插槽::

    .add 41611

非锻造职业可以使用锻造的制品 ``泰坦神铁护板``, 附魔盾牌, 提高81格挡值, 并降低 50% 被缴械的持续时间, 常用于 PvP::

    .add 44936

非制皮专业的角色可以使用的制皮物品 ``厚北地护甲片`` 为 头, 胸, 肩, 腿, 手, 脚部增加 18 耐::

    .add 38376


.. _Lv80-力量DPS-附魔物品-GM命令:

力量DPS (武器, 狂暴战, 惩戒骑, 死亡骑士)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 添加物品命令
      - 说明
    * - ::

            /target player
            .add 44493
            .add 44463
            .add 44465
            .add 44815
            .add 44458
            .add 38986
            .add 39003
            .add 44149
            .add 38374
            .add 44133
            /targetlasttarget
      - ::

            /target player
            .add 44493 单手武器 狂暴
            .add 44463 双手武器 110AP
            .add 44465 胸甲 10属性
            .add 44815 护腕 50AP
            .add 44458 手套 44AP
            .add 38986 靴子 12命中致命
            .add 39003 披风 23速度
            .add 44149 头部 黯刃骑士团
            .add 38374 裤子 制皮附魔
            .add 44133 肩部 霍迪尔之子
            /targetlasttarget


.. _Lv80-敏捷DPS-附魔物品-GM命令:

敏捷DPS (盗贼, 猎人, 增强萨满, 野德)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 添加物品命令
      - 说明
    * - ::

            /target player
            .add 44493
            .add 38995
            .add 44465
            .add 44815
            .add 38967
            .add 38976
            .add 44457
            .add 44149
            .add 38374
            .add 44133
            /targetlasttarget
      - ::

            /target player
            .add 44493 单手武器 狂暴
            .add 38995 双手武器 26敏
            .add 44465 胸甲 10属性
            .add 44815 护腕 50AP
            .add 38967 手套 20敏
            .add 38976 靴子 16敏
            .add 44457 披风 22敏捷
            .add 44149 头部 黯刃骑士团
            .add 38374 裤子 制皮附魔
            .add 44133 肩部 霍迪尔之子
            /targetlasttarget


.. _Lv80-法系DPS-附魔物品-GM命令:

法系DPS (法师, 术士, 暗牧, 平衡德, 元素萨)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 添加物品命令
      - 说明
    * - ::

            /target player
            .add 43987
            .add 45056
            .add 44465
            .add 44470
            .add 38979
            .add 38986
            .add 39003
            .add 44159
            .add 41602
            .add 41604
            .add 44135
            /targetlasttarget
      - ::

            /target player
            .add 43987 武器 黑魔法
            .add 45056 法杖 81SP
            .add 44465 胸甲 10属性
            .add 44470 护腕 30法伤
            .add 38979 手套 28法伤
            .add 38986 靴子 12命中致命
            .add 39003 披风 23加速
            .add 44159 头部 祈瑞托
            .add 41602 腿部 裁缝附魔 法伤 精神
            .add 41604 腿部 裁缝附魔 法伤 耐力
            .add 44135 肩部 霍迪尔之子
            /targetlasttarget


.. _Lv80-板甲坦克-附魔物品-GM命令:

板甲坦克 (防战, 防骑, DK坦)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 添加物品命令
      - 说明
    * - ::

            /target player
            .add 44946
            .add 38954
            .add 39005
            .add 44947
            .add 38951
            .add 38966
            .add 39001
            .add 44150
            .add 38373
            .add 44136
            /targetlasttarget
      - ::

            /target player
            .add 44946 武器 50耐
            .add 38954 盾牌 20防御
            .add 39005 胸甲 275生命
            .add 44947 护腕 40耐
            .add 38951 手套 15熟练
            .add 38966 靴子 22耐力
            .add 39001 披风 225护甲
            .add 44150 头部 银白十字军
            .add 38373 裤子 制皮附魔
            .add 44136 肩部 霍迪尔之子
            /targetlasttarget


.. _Lv80-熊坦-附魔物品-GM命令:

熊坦
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
熊坦从装备获得的耐力和护甲加成非常高, 并且 ICC 后期血甲非常重要.

.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 添加物品命令
      - 说明
    * - ::

            /target player
            .add 44946
            .add 38376
            .add 44947
            .add 38376
            .add 38966
            .add 39001
            .add 44150
            .add 38373
            .add 44957
            .add 44957
            /targetlasttarget
      - ::

            /target player
            .add 44946 武器 50耐
            .add 38376 胸甲 护甲片
            .add 44947 护腕 40耐
            .add 38376 手套 护甲片
            .add 38966 靴子 22耐力
            .add 39001 披风 225护甲
            .add 44150 头部 银白十字军
            .add 38373 裤子 制皮附魔
            .add 44957 肩部 联盟 30耐
            .add 44957 肩部 部落 30耐
            /targetlasttarget


.. _Lv80-治疗-附魔物品-GM命令:

治疗 (奶骑, 奶萨, 奶德, 牧师)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 添加物品命令
      - 说明
    * - ::

            /target player
            .add 45056
            .add 44467
            .add 44455
            .add 38962
            .add 44470
            .add 38979
            .add 38961
            .add 39003
            .add 44152
            .add 41602
            .add 41604
            .add 44134
            /targetlasttarget

      - ::

            /target player
            .add 45056 法杖 81SP
            .add 44467 武器 63SP
            .add 44455 盾牌 25智
            .add 38962 胸甲 10MP5
            .add 44470 护腕 30法伤
            .add 38979 手套 28法伤
            .add 38961 靴子 18精
            .add 39003 披风 23速度
            .add 44152 头部 龙眠协调者
            .add 41602 腿部 裁缝附魔 法伤 精神
            .add 41604 腿部 裁缝附魔 法伤 耐力
            .add 44134 肩部 霍迪尔之子
            /targetlasttarget


.. _Lv80-PvP-附魔物品-GM命令:

PvP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - 阵营
      - 添加物品宏命令
      - 说明
    * - .. image:: /_static/image/faction-icon/alliance.png
      - ::

            /target player
            .add 44701
            .add 44957
            .add 44963
            /targetlasttarget

      - ::

            /target player
            .add 44701 头部 凶残角斗士秘药 联盟远征军
            .add 44957 肩部 荣誉附魔
            .add 44963 腿部 制皮附魔
            /targetlasttarget
    * - .. image:: /_static/image/faction-icon/horde.png
      - ::

            /target player
            .add 44702
            .add 44957
            .add 44963
            /targetlasttarget

      - ::

            /target player
            .add 44702 头部 凶残角斗士秘药 部落远征军
            .add 44957 肩部 荣誉附魔
            .add 44963 腿部 制皮附魔
            /targetlasttarget


燃烧的远征
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

.. _Lv70-力量DPS-附魔物品-GM命令:

力量DPS (武器, 狂暴战, 惩戒骑, 死亡骑士)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
::

    .add 44493 单手武器 狂暴
    .add 44463 双手武器 110AP
    .add 44465 胸甲 10属性
    .add 44815 护腕 50AP
    .add 44458 手套 44AP
    .add 38986 靴子 12命中致命
    .add 39003 披风 23速度
    .add 29192 头部 塞纳里奥远征队
    .add 29535 裤子 制皮附魔
    .add 44133 肩部 霍迪尔之子


.. _Lv70-敏捷DPS-附魔物品-GM命令:

敏捷DPS (盗贼, 猎人, 增强萨满, 野德)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
::

    .add 44493 单手武器 狂暴
    .add 38995 双手武器 26敏
    .add 44465 胸甲 10属性
    .add 44815 护腕 50AP
    .add 38967 手套 20敏
    .add 38976 靴子 16敏
    .add 44457 披风 22敏捷
    .add 29192 头部 塞纳里奥远征队
    .add 29535 裤子 制皮附魔
    .add 44133 肩部 霍迪尔之子


.. _Lv70-法系DPS-附魔物品-GM命令:

法系DPS (法师, 术士, 暗牧, 平衡德, 元素萨)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
::

    .add 43987 武器 黑魔法
    .add 45056 法杖 81SP
    .add 44465 胸甲 10属性
    .add 44470 护腕 30法伤
    .add 38979 手套 28法伤
    .add 38986 靴子 12命中致命
    .add 39003 披风 23加速
    .add 29191 头部 沙塔斯城
    .add 24274 腿部 裁缝附魔
    .add 44135 肩部 霍迪尔之子


.. _Lv70-板甲坦克-附魔物品-GM命令:

板甲坦克 (防战, 防骑)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
::

    .add 44946 武器 50耐
    .add 38954 盾牌 20防御
    .add 39005 胸甲 275生命
    .add 44947 护腕 40耐
    .add 38951 手套 15熟练
    .add 38966 靴子 22耐力
    .add 39001 披风 225护甲
    .add 29186 头部 时光之穴
    .add 29536 裤子 制皮附魔
    .add 44136 肩部 霍迪尔之子


.. _Lv70-熊坦-附魔物品-GM命令:

熊坦
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
熊坦从装备获得的耐力和护甲加成非常高, 并且 ICC 后期血甲非常重要:

::

    .add 44946 武器 50耐
    .add 38376 胸甲 护甲片
    .add 44947 护腕 40耐
    .add 38376 手套 护甲片
    .add 38966 靴子 22耐力
    .add 39001 披风 225护甲
    .add 29186 头部 时光之穴
    .add 29536 裤子 制皮附魔
    .add 44957 肩部 联盟 30耐
    .add 44957 肩部 部落 30耐


.. _Lv70-治疗-附魔物品-GM命令:

治疗 (奶骑, 奶萨, 奶德, 牧师)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
::

    .add 45056 法杖 81SP
    .add 44467 武器 63SP
    .add 44455 盾牌 25智
    .add 38962 胸甲 10MP5
    .add 44470 护腕 30法伤
    .add 38979 手套 28法伤
    .add 38961 靴子 18精
    .add 39003 披风 23速度
    .add 41602 裤子 裁缝附魔
    .add 44134 肩部 霍迪尔之子

联盟::

    .add 29189 头部 荣誉堡

部落::

    .add 29190 头部 萨尔玛


经典旧世
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

注:

- 头腿最佳附魔为 :ref:`祖尔格拉布职业附魔 <ZugEnchant>`
- 肩膀最佳附魔为 :ref:`纳克萨玛斯冰龙附魔 <NaxxEnchant>`


.. _Lv60-力量DPS-附魔物品-GM命令:

力量DPS 力量DPS (武器, 狂暴战, 惩戒骑, 死亡骑士)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
经典旧世没有设计武器战士和惩戒骑士的DPS输出的附魔, 祖格的附魔不适用, 所以只能用厄运头腿附魔了:

.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 添加物品命令
      - 说明
    * - ::

            /target player
            .add 38870
            .add 38873
            .add 38891
            .add 38865
            .add 38854
            .add 38857
            .add 38862
            .add 11645
            .add 23548
            .add 11645
            /targetlasttarget

      - ::

            /target player
            .add 38870 主手 5伤害
            .add 38873 副手 十字军
            .add 38891 披风 15火炕
            .add 38865 胸部 4全属性
            .add 38854 护腕 9力
            .add 38857 手 7力
            .add 38862 脚 7耐
            .add 11645 头 8力
            .add 23548 肩部 冰龙附魔
            .add 11645 腿部 8力量
            /targetlasttarget


.. _Lv60-敏捷DPS-附魔物品-GM命令:

敏捷DPS (盗贼, 猎人, 增强萨满, 野德)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 10 10 60
    :header-rows: 1

    * - 职业
      - 注释
      - 添加物品宏命令
      - 说明
    * - .. image:: /_static/image/class-icon/06-Rogue.png
      - 盗贼, 武器伤害很重要, 攻击频率高, 容易触发十字军效果
      - ::

            /target player
            .add 38870
            .add 38873
            .add 19784 2
            .add 38891
            .add 38865
            .add 38855
            .add 38856
            .add 38863
            .add 23548
            /targetlasttarget

      - ::

            /target player
            .add 38870 主手 5伤害
            .add 38873 副手 十字军
            .add 19784 2 头 腿 祖格附魔
            .add 38891 披风 15火炕
            .add 38865 胸部 4全属性
            .add 38855 护腕 9耐
            .add 38856 手套 7敏
            .add 38863 靴子 7敏
            .add 23548 肩部 冰龙附魔
            /targetlasttarget
    * - .. image:: /_static/image/class-icon/04-Hunter.png
      - 猎人, 敏捷收益高
      - ::

            /target player
            .add 38880 2
            .add 19785 2
            .add 38891
            .add 38865
            .add 38855
            .add 38856
            .add 38863
            .add 23548
            /targetlasttarget

      - ::

            /target player
            .add 38880 2 主手 副手 15敏
            .add 19785 2 头 腿 祖格附魔
            .add 38891 披风 15火炕
            .add 38865 胸部 4全属性
            .add 38855 护腕 9耐
            .add 38856 手套 7敏
            .add 38863 靴子 7敏
            .add 23548 肩部 冰龙附魔
            /targetlasttarget
    * - .. image:: /_static/image/class-icon/05-Shaman.png
      - 增强萨和野德没有对应的祖格附魔, 只能用厄运的
      - ::

            /target player
            .add 38880 2
            .add 11647 2
            .add 38891
            .add 38865
            .add 38855
            .add 38856
            .add 38863
            .add 23548
            /targetlasttarget

      - ::

            /target player
            .add 38880 2 主手 副手 15敏
            .add 11647 2 头 腿 8敏捷 厄运附魔
            .add 38891 披风 15火炕
            .add 38865 胸部 4全属性
            .add 38855 护腕 9耐
            .add 38856 手套 7敏
            .add 38863 靴子 7敏
            .add 23548 肩部 冰龙附魔
            /targetlasttarget


.. _Lv60-法系DPS-附魔物品-GM命令:

法系DPS (法师, 术士, 暗牧, 平衡德, 元素萨)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - 职业
      - 添加物品命令
      - 说明
    * - .. image:: /_static/image/class-icon/05-Shaman.png
      - ::

            /target player
            .add 19786 2
            .add 38877
            .add 38860
            .add 38891
            .add 38867
            .add 38882
            .add 38889
            .add 38862
            .add 23545
            /targetlasttarget
      - ::

            /target player
            .add 19786 2 头 腿 萨满头 祖格附魔
            .add 38877 武器 30SP
            .add 38860 盾牌 4MP5
            .add 38891 披风 15火炕
            .add 38867 胸部 100法力
            .add 38882 护腕 15SP
            .add 38889 手套 16SP
            .add 38862 靴子 7耐
            .add 23545 肩部 冰龙附魔
            /targetlasttarget
    * - .. image:: /_static/image/class-icon/07-Druid.png
      - ::

            /target player
            .add 19790 2
            .add 38877
            .add 38860
            .add 38891
            .add 38867
            .add 38882
            .add 38889
            .add 38862
            .add 23545
            /targetlasttarget
      - ::

            /target player
            .add 19790 2 头 腿 德鲁伊 祖格附魔
            .add 38877 武器 30SP
            .add 38860 盾牌 4MP5
            .add 38891 披风 15火炕
            .add 38867 胸部 100法力
            .add 38882 护腕 15SP
            .add 38889 手套 16SP
            .add 38862 靴子 7耐
            .add 23545 肩部 冰龙附魔
            /targetlasttarget
    * - .. image:: /_static/image/class-icon/08-Mage.png
      - ::

            /target player
            .add 19787
            .add 38877
            .add 38860
            .add 38891
            .add 38867
            .add 38882
            .add 38889
            .add 38862
            .add 23545
            /targetlasttarget
      - ::

            /target player
            .add 19787 2 头 腿 法师 祖格附魔
            .add 38877 武器 30SP
            .add 38860 盾牌 4MP5
            .add 38891 披风 15火炕
            .add 38867 胸部 100法力
            .add 38882 护腕 15SP
            .add 38889 手套 16SP
            .add 38862 靴子 7耐
            .add 23545 肩部 冰龙附魔
            /targetlasttarget
    * - .. image:: /_static/image/class-icon/09-Warlock.png
      - ::

            /target player
            .add 19788 2
            .add 38877
            .add 38860
            .add 38891
            .add 38867
            .add 38882
            .add 38889
            .add 38862
            .add 23545
            /targetlasttarget
      - ::

            /target player
            .add 19788 2 头 腿 术士 祖格附魔
            .add 38877 武器 30SP
            .add 38860 盾牌 4MP5
            .add 38891 披风 15火炕
            .add 38867 胸部 100法力
            .add 38882 护腕 15SP
            .add 38889 手套 16SP
            .add 38862 靴子 7耐
            .add 23545 肩部 冰龙附魔
            /targetlasttarget
    * - .. image:: /_static/image/class-icon/10-Priest.png
      - ::

            /target player
            .add 19789 2
            .add 38877
            .add 38860
            .add 38891
            .add 38867
            .add 38882
            .add 38889
            .add 38862
            .add 23545
            /targetlasttarget
      - ::

            /target player
            .add 19789 2 头 腿 牧师 祖格附魔
            .add 38877 武器 30SP
            .add 38860 盾牌 4MP5
            .add 38891 披风 15火炕
            .add 38867 胸部 100法力
            .add 38882 护腕 15SP
            .add 38889 手套 16SP
            .add 38862 靴子 7耐
            .add 23545 肩部 冰龙附魔
            /targetlasttarget


.. _Lv60-坦克-附魔物品-GM命令:

坦克 (防战, 防骑, 死亡骑士, 熊坦)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - 职业
      - 添加物品命令
      - 说明
    * - .. image:: /_static/image/class-icon/01-Warrior.png
      - ::

            /target player
            .add 19782 2
            .add 38880 2
            .add 38861
            .add 38859
            .add 38866
            .add 38855
            .add 38890
            .add 38862
            .add 23549
            /targetlasttarget
      - ::

            /target player
            .add 19782 2 头 腿 防战 祖格附魔
            .add 38880 武器 15敏
            .add 38861 盾牌 7耐
            .add 38859 披风 70护甲
            .add 38866 胸部 100生命
            .add 38855 护腕 9耐
            .add 38890 手套 15敏
            .add 38862 靴子 7耐
            .add 23549 肩部 冰龙附魔
            /targetlasttarget
    * - .. image:: /_static/image/class-icon/02-Paladin.png
      - ::

            /target player
            .add 19783 2
            .add 38880 2
            .add 38861
            .add 38859
            .add 38866
            .add 38855
            .add 38890
            .add 38862
            .add 23549
            /targetlasttarget
      - ::

            /target player
            .add 19783 2 头 腿 防骑 祖格附魔
            .add 38880 武器 15敏
            .add 38861 盾牌 7耐
            .add 38859 披风 70护甲
            .add 38866 胸部 100生命
            .add 38855 护腕 9耐
            .add 38890 手套 15敏
            .add 38862 靴子 7耐
            .add 23549 肩部 冰龙附魔
            /targetlasttarget
    * - .. image:: /_static/image/class-icon/03-DeathKnight.png
      - ::

            /target player
            .add 11642 2
            .add 38880 2
            .add 38859
            .add 38866
            .add 38855
            .add 38890
            .add 38862
            .add 23549
            /targetlasttarget
      - ::

            /target player
            .add 11642 2 头 腿 100生命 厄运附魔
            .add 38880 2 武器 15敏
            .add 38859 披风 70护甲
            .add 38866 胸部 100生命
            .add 38855 护腕 9耐
            .add 38890 手套 15敏
            .add 38862 靴子 7耐
            .add 23549 肩部 冰龙附魔
            /targetlasttarget
    * - .. image:: /_static/image/class-icon/07-Druid.png
      - ::

            /target player
            .add 11642 2
            .add 38880
            .add 38859
            .add 38866
            .add 38855
            .add 38890
            .add 38862
            .add 23549
            /targetlasttarget
      - ::

            /target player
            .add 11642 2 头 腿 100生命 厄运附魔
            .add 38880 武器 15敏
            .add 38859 披风 70护甲
            .add 38866 胸部 100生命
            .add 38855 护腕 9耐
            .add 38890 手套 15敏
            .add 38862 靴子 7耐
            .add 23549 肩部 冰龙附魔
            /targetlasttarget


.. _所有附魔物品速查:

所有附魔物品速查
------------------------------------------------------------------------------
.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

.. jinja:: doc_data

    {% for item in doc_data.lt_list_item_enhancement() %}
    {{ item.render() }}
    {% endfor %}
