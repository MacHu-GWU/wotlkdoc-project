.. _常用通用宏命令:

常用通用宏命令
==============================================================================

.. contents::
    :local:


根据当前的目标是敌方或我方, 对不同的目标施放单个治疗技能或驱散技能类
------------------------------------------------------------------------------
无论什么时候, 按住Alt键治疗自己. 不按住Alt键时, 鼠标悬停或者选择目标时, 如果目标是右方, 则治疗友方目标. 如果是敌方, 则治疗敌方的目标::

    #showtooltips
    /cast [modifier:alt,target=player][target=mouseover,help][help][target=targettarget,help][] 快速治疗

条件判断的先后顺序为:

1. ``[modifier:alt,target=player]``: 只要按下了Alt键, 则是对自己释放治疗
2. #1不成立, 检查 ``[target=mouseover,help]``: 如果鼠标悬停是友方, 则对其释放治疗
3. #2不成立, 检查 ``[help]``: 如果目标是友方, 则对其释放治疗 (在目标是敌方的时候, 该条件不生效)
4. #3不成立, 检查 ``[target=targettarget,help]``: 如果目标的目标是友方, 则对其释放治疗
5. #4 不成立, 其他情况下, 按照正常释放治疗


根据当前的目标是敌方或我方, 对不同的目标施放单个治疗技能或驱散技能类 用 Alt 绑定多个技能
------------------------------------------------------------------------------

**注意**, 由于我们需要用按下 Alt 来释放另一个技能, 不按 Alt 释放原技能, 所以我们必须取消 ``[modifier:alt,target=player]`` 这一用于对自己释放的语句.

**注意**, 绑定两个技能时, 按下 Alt 键才能看到的技能最好是无 CD 技能, 这样就不用检测其冷却时间了.

该命令的功能有, 鼠标悬停, 治疗友方, 治疗敌方的目标, 正常治疗. 不过同时绑定了两个治疗技能.

治疗版本::

    #showtooltips
    /cast [modifier:alt,target=mouseover,help][modifier:alt,help][modifier:alt,target=targettarget,help][modifier:alt] 圣光术; [target=mouseover,help][help][target=targettarget,help][] 圣光闪现

驱散版本::

    #showtooltips
    /cast [modifier:alt,target=mouseover,help][modifier:alt,help][modifier:alt,target=targettarget,help][modifier:alt] 群体驱散; [target=mouseover,help][help][target=targettarget,help][] 驱散魔法


智能释放 对敌人释放的技能
------------------------------------------------------------------------------
- 如果目标是 **敌人**, 则对目标释放.
- 如果目标的目标是 **敌人**, 则对目标的目标施放.

::

    #showtooltips
    /cast [harm][target=targettarget,harm][] 魔法反制

    #showtooltips
    /cast [harm][target=targettarget,harm][] 寒冰箭


根据当前的目标是敌方或我方, 对其使用不同的技能
------------------------------------------------------------------------------

::

    #showtooltips
    /cast [harm]


按优先级攻击视野内的多个不同的怪
------------------------------------------------------------------------------

原理: /tar [noexists][dead] 命令只有在你没有目标, 或是目标已经死了的情况下才会执行. /tar 命令本身永远优先选择 活的怪, 如果有多个活的怪优先选择最近的.

::

    /cleartarget
    /tar [noexists][dead] 第一优先
    /tar [noexists][dead] 第二优先
    /cast Lightning Bolt



AH (交易相关命令)
------------------------------------------------------------------------------
AH是Auction House的缩写.


One Click Buy (一键一口价购买)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: AH_OneClickBuy.png

在拍卖行选中物品后, 按下该宏一键一口价购买物品. **注意不要买到天价物品!**::

    /click BrowseBuyoutButton
    /click StaticPopup1Button1


Wants to Buy/Sell (喊话收购, 出售)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: AH_WTB.png
a
将item_id和喊话内容稍作修改, 即可在喊话中插入物品链接, 系统限制一次喊话不得超过3个物品链接::

    /run local a,a=GetItemInfo(item_id); local b,b=GetItemInfo(item_id); SendChatMessage("Buy "..a.." 60G/Each, "..b.." 30G/Each, W me or COD me.","channel",nil,2)


Bid This (一键竞标)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: AH_BidThis.png

在拍卖行选中物品后, 按下该宏对物品竞标. **注意不要买到天价物品!**::

    /click BrowseBidButton
    /click StaticPopup1Button1


MultiBoxing (多开)
------------------------------------------------------------------------------
MB是MultiBoxing的缩写.


Follow Focus (跟随焦点)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: MB_FollowFocus.png

跟随焦点目标::

    /follow focus


Assist Focus (协助焦点)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: MB_AssistFocus.png

协助焦点, 即选择焦点的目标::

    /assist focus


Set Focus (设置焦点)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: MB_SetFocus.png

设置某位玩家为焦点::

    /setfocus [target=CharName]


PvP (玩家对玩家)
------------------------------------------------------------------------------

Interrupt (打断)

/target