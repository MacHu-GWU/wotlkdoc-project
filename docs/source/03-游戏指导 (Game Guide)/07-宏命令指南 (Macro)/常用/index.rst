治疗类
------------------------------------------------------------------------------


智能
------------------------------------------------------------------------------
无论什么时候, 按住Alt键治疗自己. 不按住Alt键时, 鼠标悬停或者选择目标时, 如果目标是右方, 则治疗友方目标. 如果是敌方, 则治疗敌方的目标::

    #showtooltips
    /cast [modifier:alt,target=player][target=mouseover,help][help][target=targettarget,help][] 快速治疗

条件判断的先后顺序为:

- 只要按下了Alt键, 则是对自己释放治疗
- 如果鼠标悬停是友方, 则对其释放治疗
- 如果目标是友方, 则对其释放治疗 (在目标是敌方的时候, 该条件不生效)
- 如果目标的目标是友方, 则对其释放治疗
- 其他情况下, 按照正常释放治疗


- 如果目标是 **友方**, 则对目标施放.
- 如果目标的目标是 **友方**, 则对目标的目标施放.

    #showtooltips
    /cast [help][target=targettarget,help][] 圣光术

    #showtooltips
    /cast [help][target=targettarget,help][] 净化术


智能释放 对敌人释放的技能
------------------------------------------------------------------------------
- 如果目标是 **敌人**, 则对目标释放.
- 如果目标的目标是 **敌人**, 则对目标的目标施放.

::

    #showtooltips
    /cast [harm][target=targettarget,harm][] 魔法反制

    #showtooltips
    /cast [harm][target=targettarget,harm][] 寒冰箭


General (通用宏命令)
==============================================================================


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