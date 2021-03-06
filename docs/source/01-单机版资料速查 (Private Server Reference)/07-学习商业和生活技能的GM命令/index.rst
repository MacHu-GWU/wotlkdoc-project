.. _学习商业和生活技能的GM命令:

学习商业和生活技能的GM命令 (Learn Tradeskill GM Command)
===============================================================================

.. contents:: 目录
    :local:

.. image:: /_static/image/trade-skill/herbalism.png
    :target: 草药学GM命令_
.. image:: /_static/image/trade-skill/alchemy.png
    :target: 炼金术GM命令_
.. image:: /_static/image/trade-skill/skinning.png
    :target: 剥皮GM命令_
.. image:: /_static/image/trade-skill/leatherworking.png
    :target: 制皮GM命令_
.. image:: /_static/image/trade-skill/mining.png
    :target: 采矿GM命令_
.. image:: /_static/image/trade-skill/blacksmithing.png
    :target: 锻造GM命令_
.. image:: /_static/image/trade-skill/tailoring.png
    :target: 裁缝GM命令_
.. image:: /_static/image/trade-skill/enchanting.png
    :target: 附魔GM命令_
.. image:: /_static/image/trade-skill/engineering.png
    :target: 工程学GM命令_
.. image:: /_static/image/trade-skill/jewelcrafting.png
    :target: 珠宝加工GM命令_
.. image:: /_static/image/trade-skill/inscription.png
    :target: 铭文学GM命令_

------

.. image:: /_static/image/trade-skill/first-aid.png
    :target: 急救GM命令_
.. image:: /_static/image/trade-skill/fishing.png
    :target: 钓鱼GM命令_
.. image:: /_static/image/trade-skill/cooking.png
    :target: 烹饪GM命令_
.. image:: /_static/image/icon/inv_misc_key_01.png
    :target: 开锁GM命令_


商业和生活技能的代码属于 Skill (技能类), 不属于 Spell (法术类). 但是和 :ref:`学习武器和防具技能 <学习武器和防具技能的GM命令>` 类似, 与 ``商业技能训练师`` 对话时, 是通过对玩家施放一个法术, 来提高玩家的商业技能等级上线的. 这些法术属于 Spell.

使用 ``.learn <spell_id>`` 即可习得该技能, 使用 ``.setskill <skill_id> <level>`` 即可设定该技能的等级。

.. note::

    - 配方出处查询请参考插件 :ref:`AckisRecipeList`.
    - 配方的详细信息, 例如技能等级提升情况, 请参考插件 :ref:`TradeskillInfo`.


学习 ``商业技能`` 的GM命令
-------------------------------------------------------------------------------

.. note::

    注: 如果你想要学到最高等级, 你只需要 ``宗师`` 的那条命令, 和 ``.setskill`` 那条命令就可以了. 学了宗师级技能后, 低等级技能会自动习得.


.. _草药学GM命令:

草药学 (Herbalism)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/herbalism.png

::

    .learn 2366 初级
    .learn 2368 中级
    .learn 3570 高级
    .learn 11993 专家
    .learn 28695 大师
    .learn 50300 宗师
    .setskill 182 450


.. _炼金术GM命令:

炼金术 (Alchemy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/alchemy.png

::

    .learn 2259 初级
    .learn 3101 中级
    .learn 3464 高级
    .learn 11611 专家
    .learn 28597 大师
    .learn 50303 宗师
    .setskill 171 450


.. _剥皮GM命令:

剥皮 (Skinning)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/skinning.png

::

    .learn 8613 初级
    .learn 8617 中级
    .learn 8618 高级
    .learn 10768 专家
    .learn 32678 大师
    .learn 50305 宗师
    .setskill 393 450


.. _制皮GM命令:

制皮 (Leatherworking)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/leatherworking.png

::

    .learn 2108 初级
    .learn 3104 中级
    .learn 3811 高级
    .learn 10662 专家
    .learn 32549 大师
    .learn 51302 宗师
    .setskill 165 450


.. _采矿GM命令:

采矿 (Mining)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/mining.png

::

    .learn 2575 初级
    .learn 2576 中级
    .learn 3564 高级
    .learn 10248 专家
    .learn 29354 大师
    .learn 50310 宗师
    .setskill 186 450


.. _锻造GM命令:

锻造 (Blacksmithing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/blacksmithing.png

::

    .learn 2018 初级
    .learn 3100 中级
    .learn 3538 高级
    .learn 9785 专家
    .learn 29844 大师
    .learn 51300 宗师
    .setskill 164 450


.. _裁缝GM命令:

裁缝 (Tailoring)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/tailoring.png

::

    .learn 3908 初级
    .learn 3909 中级
    .learn 3910 高级
    .learn 12180 专家
    .learn 26790 大师
    .learn 51309 宗师
    .setskill 197 450


.. _附魔GM命令:

附魔 (Enchanting)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/enchanting.png

::

    .learn 7411 初级
    .learn 7412 中级
    .learn 7413 高级
    .learn 13920 专家
    .learn 28029 大师
    .learn 51313 宗师
    .setskill 333 450


.. _工程学GM命令:

工程学 (Engineering)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/engineering.png

::

    .learn 4036 初级
    .learn 4037 中级
    .learn 4038 高级
    .learn 12656 专家
    .learn 30350 大师
    .learn 51306 宗师
    .setskill 202 450


.. _珠宝加工GM命令:

珠宝加工 (Jewelcrafting)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/jewelcrafting.png

::

    .learn 25229 初级
    .learn 25230 中级
    .learn 28894 高级
    .learn 28895 专家
    .learn 28897 大师
    .learn 51311 宗师
    .setskill 755 450


.. _铭文学GM命令:

铭文学 (Inscription)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/inscription.png

::

    .learn 45357 初级
    .learn 45358 中级
    .learn 45359 高级
    .learn 45360 专家
    .learn 45361 大师
    .learn 45363 宗师
    .setskill 773 450


学习 ``生活技能`` 的GM命令
-------------------------------------------------------------------------------


.. _急救GM命令:

急救 (First Aid)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/first-aid.png

::

    .learn 3273 初级
    .learn 3274 中级
    .learn 7924 高级
    .learn 10846 专家
    .learn 27028 大师
    .learn 45542 宗师
    .setskill 129 450


.. _钓鱼GM命令:

钓鱼 (Fishing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/fishing.png

::

    .learn 7620 初级
    .learn 7731 中级
    .learn 7732 高级
    .learn 18248 专家
    .learn 33095 大师
    .learn 64484 宗师
    .setskill 356 450


.. _烹饪GM命令:

烹饪 (Cooking)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/trade-skill/cooking.png

::

    .learn 2550 初级
    .learn 3102 中级
    .learn 3413 高级
    .learn 18260 专家
    .learn 33359 大师
    .learn 51296 宗师
    .setskill 185 450


.. _开锁GM命令:

开锁
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/icon/inv_misc_key_01.png

::

    .learn 1804 开锁
    .setskill 633 400 # 60级最高300, 70级最高350, 80级最高400


学会所有生活技能的宏命令
------------------------------------------------------------------------------
::

    .learn 64484 钓鱼
    .setskill 356 450
    .learn 51296 烹饪
    .setskill 185 450
    .learn 45542 急救
    .setskill 129 450
