.. _牧师宏命令:

牧师宏命令
==============================================================================

.. contents::
    :local:


默认双天赋时的第一套天赋为 暗牧 天赋, 第二套天赋为 神圣/戒律 天赋. 这样 [spec:1] 代表 暗牧, [spec:2] 代表 治疗天赋.

注意: 暗言术痛 不受急速的影响, 噬灵瘟疫 和 吸血鬼之触 受到急速的影响.


一键自我 Buff 宏
------------------------------------------------------------------------------

- 暗牧天赋下: 如果没有暗影形态, 则进入 暗影形态, 然后依次对自己施放 吸血鬼的拥抱, 心灵之火, 真言术：韧, 神圣之灵, 暗影防护
- 治疗天赋下: 依次对自己施放 心灵之火, 真言术：韧, 神圣之灵, 暗影防护

.. code-block:: python

    #showtooltip
    /target player
    /cast [nostance,spec:1] 暗影形态
    /castsequence [spec:1] reset=target 吸血鬼的拥抱, 心灵之火, 真言术：韧, 神圣之灵, 暗影防护; [spec:2] reset=target 心灵之火, 真言术：韧, 神圣之灵, 暗影防护



驱散, 驱除疾病
------------------------------------------------------------------------------

- 对目标施放 驱散, 按下 Alt 键为智能施放 驱除疾病. 由于 驱散 技能可以对敌人也可以对自己释放, 所以交给玩家自行判断.

.. code-block:: python

    #showtooltip
    /cast [modifier:alt,target=mouseover,help][modifier:alt,help][modifier:alt,target=targettarget,help][modifier:alt] 驱除疾病; 驱散魔法


智能 快速治疗, 强效治疗术 (键位 X)
------------------------------------------------------------------------------

- 智能施放 快速治疗, 按下 Alt 键为 强效治疗术.

.. code-block:: python

    #showtooltips
    /cast [mod:alt,target=mouseover,help][mod:alt,help][mod:alt,target=targettarget,help][mod:alt] 强效治疗术; [target=mouseover,help][help][target=targettarget,help][] 快速治疗


无脑输出宏
------------------------------------------------------------------------------
.. image:: 无脑输出宏.png

无脑输出宏::

    #showtooltips
    /cast [nostance] 暗影形态
    /castsequence [nochanneling] reset=target 吸血鬼之触, 精神鞭笞, 精神鞭笞, 精神鞭笞, 精神鞭笞


暗言术：痛, 暗言术：灭, 联结治疗 (键位 1)
------------------------------------------------------------------------------

- 当前目标为友方或无目标时, 施放 恢复 (按下 Alt 为 强效治疗术)
- 当前目标为敌方, 施放 痛 (按下 Alt 为 灭)

.. code-block:: python

    #showtooltip
    /cast [mod:alt,help] 联结治疗; [mod:alt,harm] 暗言术：灭; [harm]暗言术：痛; [mod:alt] 联结治疗


精神鞭笞, 惩击, 精神灼烧 (键位 2)
------------------------------------------------------------------------------

- 暗牧天赋下: 精神鞭笞, 按下 Alt 键为 精神灼烧
- 治疗天赋下: 惩击, 按下 Alt 键为 精神灼烧

.. code-block:: python

    #showtooltip
    /cast [mod:alt] 精神灼烧; [spec:1] 精神鞭笞; [spec:2] 惩击


快速治疗, 联结治疗, 精神鞭笞, 吸血鬼之触 (键位 3)
------------------------------------------------------------------------------

- 当前目标为友方或无目标时, 施放 神圣新星 (按下 Alt 为 治疗祷言)
- 当前目标为敌方时, 施放 心灵震爆 (按下 Alt 为 噬灵疫病)

.. code-block:: python

    #showtooltip
    /cast [mod:alt,help] 治疗祷言; [help] 神圣新星; [mod:alt,harm] 噬灵疫病; [harm] 心灵震爆; [mod:alt] 治疗祷言; [] 神圣新星
