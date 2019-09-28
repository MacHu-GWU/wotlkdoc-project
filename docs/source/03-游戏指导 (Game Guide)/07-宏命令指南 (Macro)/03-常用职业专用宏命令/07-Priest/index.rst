.. _牧师宏命令:

牧师宏命令
==============================================================================

.. contents::
    :local:


驱散
------------------------------------------------------------------------------
.. image:: 驱散.png

取消当前施法, 如果目标是友方, 则驱散目标; 如果目标是敌方, 则驱散目标的目标::

    #showtooltips
    /stopcasting
    /cast [help] 驱散; [target=targettarget, harm] 驱散


智能快速治疗
------------------------------------------------------------------------------
.. image:: 智能快速治疗.png

智能快速治疗; 如果鼠标悬停, 则治疗悬停目标; 如果是敌方, 则治疗目标的目标, 如果是右方, 则治疗之::

    #showtooltips
    /stopcasting
    /cast [modifier:alt,target=player][target=mouseover,help][help][target=targettarget,help][] 快速治疗


无脑输出宏
------------------------------------------------------------------------------
.. image:: 无脑输出宏.png

无脑输出宏::

    #showtooltips
    /cast [nostance] 暗影形态
    /castsequence [nochanneling] reset=target 吸血鬼之触, 心灵震爆, 精神鞭笞, 精神鞭笞, 精神鞭笞, 精神鞭笞


恢复, 强效治疗, 暗言术痛, 暗言术灭 (键位 1)
------------------------------------------------------------------------------

- 当前目标为友方或无目标时, 施放 恢复 (按下 Alt 为 强效治疗术)
- 当前目标为敌方, 施放 痛 (按下 Alt 为 灭)

.. code-block:: python

    #showtooltip
    /cast [mod:alt,help] 强效治疗术; [mod:alt,harm] 暗言术：灭; [help] 恢复; [harm] 暗言术：痛; [mod:alt] 强效治疗术; [] 恢复


神圣新星, 治疗祷言, 心灵震爆, 精神灼烧 (键位 2)
------------------------------------------------------------------------------

- 当前目标为友方或无目标时, 施放 神圣新星 (按下 Alt 为 治疗祷言)
- 当前目标为敌方, 施放 心灵震爆 (按下 Alt 为 精神灼烧)

.. code-block:: python

    #showtooltip
    /cast [mod:alt,help] 治疗祷言; [mod:alt,harm] 精神灼烧; [help] 神圣新星; [harm] 心灵震爆; [mod:alt] 治疗祷言; [] 神圣新星


快速治疗, 联结治疗, 精神鞭笞, 吸血鬼之触 (键位 3)
------------------------------------------------------------------------------

- 当前目标为友方或无目标时, 施放 快速治疗 (按下 Alt 为 联结治疗)
- 当前目标为敌方, 施放 精神鞭笞 (按下 Alt 为 吸血鬼之触)

.. code-block:: python

    #showtooltip
    /cast [mod:alt,help] 联结治疗; [mod:alt,harm] 吸血鬼之触; [help] 快速治疗; [harm] 精神鞭笞; [mod:alt] 联结治疗; [] 快速治疗


快速治疗 强效治疗术
------------------------------------------------------------------------------

.. code-block:: python

    #showtooltips
    /cast [mod:alt,target=mouseover,help][mod:alt,help][mod:alt,target=targettarget,help][mod:alt] 强效治疗术; [target=mouseover,help][help][target=targettarget,help][] 快速治疗


驱散魔法 群体驱散
------------------------------------------------------------------------------

.. code-block:: python

    #showtooltips
    /cast [mod:alt,target=mouseover,help][mod:alt,help][mod:alt,target=targettarget,help][mod:alt] 群体驱散; [target=mouseover,help][help][target=targettarget,help][] 驱散魔法