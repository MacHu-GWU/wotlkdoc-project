.. _宏_控制宠物:

控制宠物
------------------------------------------------------------------------------
之前在讲施放技能的时候提到过，使用/cast命令可以施放宠物的技能。玻璃渣把法师的水宝宝的霜星起名叫 “冰冻术” 就是为了避免和法师自身的 “冰霜新星” 技能冲突，从而导致不能在宏内使用。但是有宠物的职业会发现，如果宏只能施放技能的话，甚至还不如宠物技能栏的功能。别急，燃烧的远征中，新增了以下这些宏指令。


``/petattack``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
让你的宠物去攻击你的当前目标。当然，在命令后加参数可以指定攻击的对象。


``/petfollow``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
宠物切换到跟随状态，同时取消攻击。


``/petpassive``, ``/petdefensive`` 和 ``/petaggressive``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
宠物切换被动、防御和主动攻击状态。同宠物技能栏上的最后3个按钮。


``/petautocaston`` 和 ``/petautocastoff``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
打开/关闭宠物技能的自动施放。例如::

    /petautocaston 折磨
    /petautocastoff 受难

不过美中不足，没有直接切换自动施放状态的宏命令，我将在后面“模拟点击”部分提到一个解决方法。
