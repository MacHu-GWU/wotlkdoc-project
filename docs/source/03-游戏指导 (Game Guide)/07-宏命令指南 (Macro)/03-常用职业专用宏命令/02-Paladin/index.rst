.. _圣骑士宏命令:

圣骑士宏命令
==============================================================================

:download:`下载圣骑士宏命令缓存文件 <macros-cache.txt>`, 将其放在 ``WTF/Account/<account_name>/<server_name>/<char_name>/macros-cache.txt`` 下.

.. contents::
    :local:

默认双天赋时的第一套天赋为 惩戒 天赋, 第二套天赋为 防护 天赋. 这样 [spec:1] 代表 暗牧, [spec:2] 代表 治疗天赋.


十字军打击, 正义之锤, 正义盾击, 圣光闪现, 圣光术 (按键 2)
------------------------------------------------------------------------------

条件:

- 第一套天赋为 ``惩戒``, 第二套天赋为 ``防护``

效果:

- ``惩戒`` 天赋下, 目标为敌人, 普通情况 和 按下Alt的情况下分别为 ``十字军打击`` 和 ``正义盾击``
- ``防护`` 天赋下, 目标为敌人, 普通情况 和 按下Alt的情况下分别为 ``正义之锤`` 和 ``正义盾击``
- 任何天赋下, 目标为友军或无目标, 普通情况 和 按下Alt的情况下分别为 ``圣光闪现`` 和 ``圣光术``

.. code-block:: python

    #showtooltip
    /startattack
    /cast [mod:alt,help] 圣光术; [mod:alt] 正义盾击; [help] 圣光闪现; [harm,spec:1] 十字军打击; [harm,spec:2] 正义之锤; [mod:alt] 圣光术; [] 圣光闪现


神圣风暴, 公正审判, 神圣之盾, 复仇者之盾 (按键 3)
------------------------------------------------------------------------------

条件:

- 第一套天赋为 ``惩戒``, 第二套天赋为 ``防护``

效果:

- ``惩戒`` 天赋下, 目标为敌人, 普通情况 和 按下Alt的情况下分别为 ``神圣风暴`` 和 ``公正审判``, 并开始自动攻击.
- ``防护`` 天赋下, 目标为敌人, 普通情况 和 按下Alt的情况下分别为 ``神圣之盾`` 和 ``复仇者之盾``, 并开始自动攻击.

.. code-block:: python

    #showtooltip
    /startattack
    /cast [mod:alt,harm,spec:1] 公正审判; [mod:alt,harm,spec:2] 复仇者之盾; [spec:1] 神圣风暴; [spec:2] 神圣之盾


奉献, 神圣愤怒 (按键 4)
------------------------------------------------------------------------------

效果:

- 普通情况 和 按下Alt的情况下分别为 ``奉献`` 和 ``神圣愤怒`` (对 10 码内的亡灵生物造成伤害并使其昏迷 3 秒), 并开始自动攻击.


.. code-block:: python

    #showtooltip
    /startattack
    /cast [mod:alt] 神圣愤怒; 奉献


智能 圣光闪现, 圣光术 (按键 X)
------------------------------------------------------------------------------

效果:

- 不用选中目标, 鼠标悬停在目标上就可以对其进行治疗:

.. code-block:: python

    #showtooltip
    /cast [mod:alt,target=mouseover] 圣光术; [target=mouseover] 圣光闪现

效果:

- 目标是敌人, 治疗敌人的目标
- 目标是友方, 治疗目标
- 鼠标悬停框体, 治疗框体
- 无目标时, 治疗自己

.. code-block:: python

    #showtooltip
    /cast [modifier:alt,target=mouseover,help][modifier:alt,help][modifier:alt,target=targettarget,help][modifier:alt] 圣光术; [target=mouseover,help][help][target=targettarget,help][] 圣光闪现
