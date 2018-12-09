.. _快速Buff宏命令:

快速Buff宏命令
==============================================================================

.. contents::
    :depth: 1
    :local:

.. image:: /_static/image/icon/spell_holy_wordfortitude.png
.. image:: /_static/image/icon/spell_holy_magicalsentry.png
.. image:: /_static/image/icon/spell_holy_divinespirit.png
.. image:: /_static/image/icon/spell_magic_greaterblessingofkings.png
.. image:: /_static/image/icon/spell_nature_regeneration.png
.. image:: /_static/image/icon/spell_nature_earthbindtotem.png

------

.. image:: /_static/image/icon/ability_warrior_sunder.png
.. image:: /_static/image/icon/ability_warrior_warcry.png
.. image:: /_static/image/icon/spell_shadow_chilltouch.png


WLK 团队副本 Buff
------------------------------------------------------------------------------

.. contents::
    :local:


物理DPS (武器/狂暴战士, 战斗/刺杀/敏锐盗贼, 猫德, 猎人, 增强萨满)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _Raid-Buff-Macro-Physical-DPS:

Buff
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - 说明
      - 宏命令
    * - .. code-block:: python

            /target player
            .aura 25898 圣骑士 王者祝福 按百分比增加全属性
            .aura 48161 牧师 真言术韧 耐
            .aura 48469 德鲁伊 野性祝福 全属性, 全抗性, 护甲
            .aura 47436 战士 战斗怒吼 AP
            .aura 48942 圣骑士 虔诚光环 护甲
            .aura 24932 德鲁伊 兽群领袖光环 物理5%爆
            .unaura 34300 德鲁伊 强化兽群领袖天赋被动 物理暴击回血
            .aura 34300 德鲁伊 强化兽群领袖天赋被动 物理暴击回血
            .aura 19506 猎人 强击光环 按百分比增加 AP
            .aura 75447 猎人 凶猛灵感 3%所有伤害
            .unaura 58646 萨满 大地之力图腾 力敏
            .aura 58646 萨满 大地之力图腾 力敏
            .aura 55610 死亡骑士 强化冰冷之爪 物理攻击加速
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 25898
            .aura 48161
            .aura 48469
            .aura 47436
            .aura 48942
            .aura 24932
            .unaura 34300
            .aura 34300
            .aura 19506
            .aura 75447
            .unaura 58646
            .aura 58646
            .aura 55610
            /targetlasttarget


.. _Raid-Debuff-Macro-Physical-DPS:

DeBuff
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - 说明
      - 宏命令
    * - .. code-block:: python

            #showtooltip
            /cast [mod:alt]嗜血术; 旋风斩
            /stopmacro [noharm]
            .aura 54499 圣骑士 十字军之心 +3%易爆
            .aura 71554 破甲 -4%护甲 叠加5次
            .aura 770 精灵之火 -5%护甲 无法潜行或隐形
            .aura 30070 战士 血性狂乱 +4%物理易伤
            .aura 33983 德鲁伊 裂伤 +30%流血效果
            .aura 20185 光明审判 击中回血 战士 盗贼 野德
            # .aura 20186 智慧审判 击中回蓝 猎人 萨满
    * - .. code-block:: python

            #showtooltip
            /cast [mod:alt]嗜血术; 旋风斩
            /stopmacro [noharm]
            .aura 54499
            .aura 71554
            .aura 770
            .aura 30070
            .aura 33983
            .aura 20185
            # .aura 20186


法系DPS (法师, 术士, 暗影牧师, 元素萨满, 平衡德鲁伊)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _Raid-Buff-Macro-Spell-DPS:

Buff
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - 说明
      - 宏命令
    * - .. code-block:: python

            /target player
            .aura 25898 圣骑士 王者祝福 按百分比增加全属性
            .aura 48161 牧师 真言术韧 耐
            .aura 48469 德鲁伊 野性祝福 全属性, 全抗性, 护甲
            .aura 42995 法师 奥术智慧 智
            .aura 48073 牧师 神圣之灵 精
            .aura 24907 德鲁伊 枭兽光环 +5%法术暴击
            .aura 75447 猎人 凶猛灵感 3%所有伤害
            .aura 19746 圣骑士 专注光环
            .unaura 58777 萨满 法力之泉光环 MP5
            .aura 58777 萨满 法力之泉光环 MP5
            .unaura 57663 萨满 天怒图腾 SP
            .aura 57663 萨满 天怒图腾 SP
            .unaura 2895 萨满 空气之怒图腾
            .aura 2895 萨满 空气之怒图腾
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 25898
            .aura 48161
            .aura 48469
            .aura 42995
            .aura 48073
            .aura 24907
            .aura 75447
            .aura 19746
            .unaura 58777
            .aura 58777
            .unaura 57663
            .aura 57663
            .unaura 2895
            .aura 2895
            /targetlasttarget


.. _Raid-Debuff-Macro-Spell-DPS:

Debuff
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

请根据需要自行修改技能名称::

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - 说明
      - 宏命令
    * - .. code-block:: python

            #showtooltip
            /cast [mod:alt]冰枪术; 寒冰箭
            /stopmacro [noharm]
            .aura 54499 圣骑士 十字军之心 +3%易爆
            .aura 47865 术士 元素诅咒 +13%法术易伤
            .aura 22959 法师 强化灼烧 +5%法术易爆
            .aura 33198 牧师 悲惨 +3% 法术易命中
            .aura 31589 法师 减速 (为欺凌弱小天赋服务)
      - .. code-block:: python

            #showtooltip
            /cast [mod:alt]冰枪术; 寒冰箭
            /stopmacro [noharm]
            .aura 54499
            .aura 47865
            .aura 22959
            .aura 33198
            .aura 31589


Tank (防御战士, 防御圣骑士, 防御死亡骑士, 熊坦德鲁伊)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _Raid-Buff-Macro-Tank:

Buff
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - 说明
      - 宏命令
    * - .. code-block:: python

            /target player
            .aura 48161 牧师 真言术韧 耐
            .aura 48469 德鲁伊 野性祝福 全属性, 全抗性, 护甲
            .aura 47440 战士 命令怒吼 HP
            .aura 25899 圣骑士 庇护祝福 免伤
            .aura 48942 圣骑士 虔诚光环 护甲
            .aura 24932 德鲁伊 兽群领袖光环 物理5%爆
            .unaura 34300 德鲁伊 强化兽群领袖天赋被动 物理暴击回血
            .aura 34300 德鲁伊 强化兽群领袖天赋被动 物理暴击回血
            .aura 19506 猎人 强击光环 按百分比增加 AP
            .aura 75447 猎人 凶猛灵感 3%所有伤害
            .unaura 58646 萨满 大地之力图腾 力敏
            .aura 58646 萨满 大地之力图腾 力敏
            .aura 55610 死亡骑士 强化冰冷之爪 物理攻击加速
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 48161
            .aura 48469
            .aura 47440
            .aura 25899
            .aura 48942
            .aura 24932
            .unaura 34300
            .aura 34300
            .aura 19506
            .aura 75447
            .unaura 58646
            .aura 58646
            .aura 55610
            /targetlasttarget


.. _Raid-Debuff-Macro-Tank:

Debuff
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

请根据需要自行修改技能名称::

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - 说明
      - 宏命令
    * - .. code-block:: python

            #showtooltip
            /cast 破甲
            /stopmacro [noharm]
            .aura 47437 战士 挫志怒吼 降低AP
            .aura 31589 法师 减速 降低移动速度, 远程攻击速度, 施法速度
            .aura 58181 德鲁伊 感染伤口 降低移动速度, 近战攻击速度
            .aura 3043 猎人 毒蝎钉刺 降低命中
      - .. code-block:: python

            #showtooltip
            /cast 破甲
            /stopmacro [noharm]
            .aura 47437
            .aura 31589
            .aura 58181
            .aura 3043


.. _Raid-Buff-Macro-Healer:

治疗 (戒律/神圣牧师, 神圣圣骑士, 恢复萨满, 恢复德鲁伊)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - 说明
      - 宏命令
    * - .. code-block:: python

            /target player
            .aura 25898 圣骑士 王者祝福 按百分比增加全属性
            .aura 48161 牧师 真言术韧 耐
            .aura 48469 德鲁伊 野性祝福 全属性, 全抗性, 护甲
            .aura 42995 法师 奥术智慧 智
            .aura 48073 牧师 神圣之灵 精
            .aura 24907 德鲁伊 枭兽光环 +5%法术暴击
            .aura 19746 圣骑士 专注光环
            .unaura 58777 萨满 法力之泉光环 MP5
            .aura 58777 萨满 法力之泉光环 MP5
            .unaura 57663 萨满 天怒图腾 SP
            .aura 57663 萨满 天怒图腾 SP
            .unaura 2895 萨满 空气之怒图腾
            .aura 2895 萨满 空气之怒图腾
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 25898
            .aura 48161
            .aura 48469
            .aura 42995
            .aura 48073
            .aura 24907
            .aura 19746
            .unaura 58777
            .aura 58777
            .unaura 57663
            .aura 57663
            .unaura 2895
            .aura 2895
            /targetlasttarget


魔武双修类职业 (惩戒骑, 增强萨)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _Raid-Buff-Physical-And-Spell-DPS:

Buff
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - 说明
      - 宏命令
    * - .. code-block:: python

            /target player
            .aura 25898 圣骑士 王者祝福 按百分比增加全属性
            .aura 48161 牧师 真言术韧 耐
            .aura 48469 德鲁伊 野性祝福 全属性, 全抗性, 护甲
            .aura 42995 法师 奥术智慧 智
            .aura 47436 战士 战斗怒吼 AP
            .aura 48942 圣骑士 虔诚光环 护甲
            .aura 24932 德鲁伊 兽群领袖光环 物理5%爆
            .unaura 34300 德鲁伊 强化兽群领袖天赋被动 物理暴击回血
            .aura 34300 德鲁伊 强化兽群领袖天赋被动 物理暴击回血
            .aura 75447 猎人 凶猛灵感 3%所有伤害
            .unaura 58646 萨满 大地之力图腾 力敏
            .aura 58646 萨满 大地之力图腾 力敏
            .unaura 57663 萨满 天怒图腾 SP
            .aura 57663 萨满 天怒图腾 SP
            .unaura 2895 萨满 空气之怒图腾
            .aura 2895 萨满 空气之怒图腾
            .aura 24907 德鲁伊 枭兽光环 +5%法术暴击
            .aura 55610 死亡骑士 强化冰冷之爪 物理攻击加速
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 25898
            .aura 48161
            .aura 48469
            .aura 42995
            .aura 47436
            .aura 48942
            .aura 24932
            .unaura 34300
            .aura 34300
            .aura 75447
            .unaura 58646
            .aura 58646
            .unaura 57663
            .aura 57663
            .unaura 2895
            .aura 2895
            .aura 24907
            .aura 55610
            /targetlasttarget


.. _Raid-Debuff-Physical-And-Spell-DPS:

Debuff
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
请根据需要自行修改技能名称:

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - 说明
      - 宏命令
    * - .. code-block:: python

            #showtooltip
            /cast [mod:alt]闪电链; 闪电箭
            /stopmacro [noharm]
            .aura 47437 战士 挫志怒吼 降低AP
            .aura 31589 法师 减速 降低移动速度, 远程攻击速度, 施法速度
            .aura 58181 德鲁伊 感染伤口 降低移动速度, 近战攻击速度
            .aura 47865 术士 元素诅咒 +13%法术易伤
            .aura 22959 法师 强化灼烧 +5%法术易爆
            .aura 33198 牧师 悲惨 +3% 法术易命中
            .aura 54499 圣骑士 十字军之心 +3%易爆
            .aura 71554 破甲 -4%护甲 叠加5次
            .aura 770 精灵之火 -5%护甲 无法潜行或隐形
            .aura 30070 战士 血性狂乱 +4%物理易伤
            .aura 33983 德鲁伊 裂伤 +30%流血效果
            .aura 20185 光明审判 击中回血 战士 盗贼 野德
            # .aura 20186 智慧审判 击中回蓝 猎人 萨满
      - .. code-block:: python

            #showtooltip
            /cast [mod:alt]闪电链; 闪电箭
            /stopmacro [noharm]
            .aura 47437
            .aura 31589
            .aura 58181
            .aura 47865
            .aura 22959
            .aura 33198
            .aura 54499
            .aura 71554
            .aura 770
            .aura 30070
            .aura 33983
            .aura 20185
            # .aura 20186


.. _Basic-Buff-Macro:

王者, 爪子, 耐, 智, 精, 力敏, 所有抗性
------------------------------------------------------------------------------

.. list-table::
    :widths: 10 10 10
    :header-rows: 1
    :class: sortable

    * - 等级
      - 说明
      - 宏命令
    * - 80
      - .. code-block:: python

            /target player
            .aura 25898 王者
            .aura 48469 爪子
            .aura 48161 耐
            .aura 42995 智
            .aura 48073 精
            .unaura 58646 力量敏捷
            .aura 58646 力量敏捷
            .aura 48947 火抗
            .aura 58744 冰抗
            .aura 48170 暗抗
            .aura 49071 自然抗
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 25898
            .aura 48469
            .aura 48161
            .aura 42995
            .aura 48073
            .unaura 58646
            .aura 58646
            .aura 48947
            .aura 58744
            .aura 48170
            .aura 49071
            /targetlasttarget
    * - 70
      - .. code-block:: python

            /target player
            .aura 25898 王者
            .aura 26990 爪子
            .aura 25389 耐
            .aura 27126 智
            .aura 25312 精
            .unaura 25527 力量敏捷
            .aura 25527 力量敏捷
            .aura 27153 火抗
            .aura 25559 冰抗
            .aura 39374 暗抗
            .aura 27045 自然抗
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 25898
            .aura 26990
            .aura 25389
            .aura 27126
            .aura 25312
            .unaura 25527
            .aura 25527
            .aura 27153
            .aura 25559
            .aura 39374
            .aura 27045
            /targetlasttarget
    * - 60
      - .. code-block:: python

            /target player
            .aura 25898 王者
            .aura 9885 爪子
            .aura 10938 耐
            .aura 10157 智
            .aura 27841 精
            .unaura 25362 力量敏捷
            .aura 25362 力量敏捷
            .aura 19900 火抗
            .aura 10477 冰抗
            .aura 27683 暗抗
            .aura 20190 自然抗
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 25898
            .aura 9885
            .aura 10938
            .aura 10157
            .aura 27841
            .unaura 25362
            .aura 25362
            .aura 19900
            .aura 10477
            .aura 27683
            .aura 20190
            /targetlasttarget
    * - 40
      - .. code-block:: python

            /target player
            .aura 25898 王者
            .aura 8907 爪子
            .aura 2791 耐
            .aura 10156 智
            .aura 14818 精
            .unaura 8163 力量敏捷
            .aura 8163 力量敏捷
            .aura 19900 火抗
            .aura 10477 冰抗
            .aura 27683 暗抗
            .aura 20190 自然抗
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 25898
            .aura 8907
            .aura 2791
            .aura 10156
            .aura 14818
            .unaura 8163
            .aura 8163
            .aura 19900
            .aura 10477
            .aura 27683
            .aura 20190
            /targetlasttarget
    * - 20
      - .. code-block:: python

            /target player
            .aura 25898 王者
            .aura 6756 爪子
            .aura 1244 耐
            .aura 1460 智
            .unaura 8075 力量敏捷
            .aura 8075 力量敏捷
            .aura 19900 火抗
            .aura 10477 冰抗
            .aura 27683 暗抗
            .aura 20190 自然抗
            /targetlasttarget
      - .. code-block:: python

            /target player
            .aura 25898
            .aura 6756
            .aura 1244
            .aura 1460
            .unaura 8075
            .aura 8075
            .aura 19900
            .aura 10477
            .aura 27683
            .aura 20190
            /targetlasttarget
