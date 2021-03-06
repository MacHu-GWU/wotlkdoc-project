娱乐用技能
==============================================================================



对玩家释放的 Buff
------------------------------------------------------------------------------


对敌人释放的 Debuff
------------------------------------------------------------------------------
.. code-block:: python

    .learn 29922 [连珠火球] 2秒施法, 3秒CD, 0法力, 20码内 1530-2070 火焰伤害
    .learn 36742 [连珠火球] 1.5秒施法, 3秒CD, 0法力, 35码内 1063-1437 火焰伤害
    .learn 38836 [连珠火球] 1.5秒施法, 3秒CD, 0法力, 40码内 2125-2875 火焰伤害

    .learn 36741 [寒冰箭雨] 1.5秒施法, 0法力, 35码内 1063-1437 冰霜伤害
    .learn 38837 [寒冰箭雨] 1.5秒施法, 0法力, 40码内 2125-2875 冰霜伤害
    .learn 58532 [寒冰箭雨] 2秒施法, 0法力, 45码内 1800-2200 冰霜伤害
    .learn 61594 [寒冰箭雨] 2秒施法, 0法力, 45码内 3780-4620 冰霜伤害

    .learn 34449 [水箭雨] 1.5秒施法, 50法力, 35码内 68-82 冰霜伤害
    .learn 59266 [水箭雨] 1.5秒施法, 50法力, 35码内 135-165 冰霜伤害

    .learn 50702 [奥术箭雨] 2.5秒施法, 90法力, 40码内 1700-2300 奥术伤害
    .learn 59212 [奥术箭雨] 2.5秒施法, 90法力, 40码内 3400-4600 奥术伤害

    .learn 56063 [奥爆术] 2秒施法, 120法力, 10码内 1350-1650 奥术伤害, 并击退
    .learn 56067 [奥爆术] 2秒施法, 120法力, 10码内 1800-2200 奥术伤害, 并击退

    .learn 39175 [暗影箭雨] 2秒施法, 160法力, 45码内 1275-1725 暗影伤害
    .learn 56064 [暗影箭雨] 3秒施法, 160法力, 30码内 1575-1925 暗影伤害
    .learn 56065 [暗影箭雨] 3秒施法, 160法力, 30码内 2250-2750 暗影伤害
    .learn 36275 [暗影箭雨] 3秒施法, 160法力, 45码内 1800-2200 暗影伤害
    .learn 38533 [暗影箭雨] 3秒施法, 160法力, 45码内 2925-3575 暗影伤害
    .learn 36275 [暗影箭雨] 1.5秒施法, 3秒CD, 0法力, 35码内 1063-1437 暗影伤害
    .learn 38840 [暗影箭雨] 1.5秒施法, 3秒CD, 0法力, 40码内 2125-2875 暗影伤害

    .learn 29293 [毒液箭雨] 2.5秒施法, 0法力, 30码内 1500-2500 自然伤害, 每5秒造成 238-262 点自然伤害, 持续15秒
    .learn 29325 [毒液箭雨] 瞬发无CD, 无公共CD, 0法力, 50码内 每3秒造成 232-268 点自然伤害, 持续24秒
    .learn 54714 [毒液箭雨] 瞬发无CD, 无公共CD, 0法力, 50码内 每3秒造成 278-322 点自然伤害, 持续24秒

    .learn 36740 [闪电箭雨] 1.5秒施法, 0法力, 35码内 1094-1406 自然伤害
    .learn 38839 [闪电箭雨] 1.5秒施法, 0法力, 40码内 2188-2812 自然伤害

    .learn 36743 [圣光箭雨] 1.5秒施法, 90法力, 35码内 1063-1437 神圣伤害
    .learn 38838 [圣光箭雨] 1.5秒施法, 90法力, 40码内 2125-2875 神圣伤害

    # 瞬发, 无CD, 无公共CD
    .learn 37109 [连珠火球] 瞬发无CD, 无公共CD, 0法力, 45码内 2125-2875 火焰伤害
    .learn 38623 [水箭雨] 瞬发无CD, 无公共CD, 50法力, 35码内 2250-2750 冰霜伤害
    .learn 38335 [水箭雨] 瞬发无CD, 无公共CD, 0法力, 45码内 2775-3225 冰霜伤害
    .learn 37129 [奥术箭雨] 瞬发无CD, 无公共CD, 110法力, 50码内 694-806 奥术伤害
    .learn 40424 [奥术箭雨] 瞬发无CD, 无公共CD, 0法力, 100码内 2775-3225 奥术伤害
    .learn 55851 [暗影箭雨] 瞬发无CD, 无公共CD, 0法力, 30码内 4625-5375 暗影伤害
    .learn 34780 [毒液箭雨] 瞬发无CD, 无公共CD, 0法力, 55码内 1444-1856 暗影伤害, 每2秒造成 289-411 点自然伤害, 持续6秒
    .learn 39340 [毒液箭雨] 瞬发无CD, 无公共CD, 0法力, 55码内 1969-2531 暗影伤害, 每2秒造成 702-988 点自然伤害, 持续6秒


玩家使用的技能
------------------------------------------------------------------------------

.. code-block:: python

    .learn 29922 [连珠火球] 2秒施法, 3秒CD, 0法力, 20码内 1530-2070 火焰伤害
    .learn 36742 [连珠火球] 1.5秒施法, 3秒CD, 0法力, 35码内 1063-1437 火焰伤害
    .learn 38836 [连珠火球] 1.5秒施法, 3秒CD, 0法力, 40码内 2125-2875 火焰伤害

    .learn 36741 [寒冰箭雨] 1.5秒施法, 0法力, 35码内 1063-1437 冰霜伤害
    .learn 38837 [寒冰箭雨] 1.5秒施法, 0法力, 40码内 2125-2875 冰霜伤害
    .learn 58532 [寒冰箭雨] 2秒施法, 0法力, 45码内 1800-2200 冰霜伤害
    .learn 61594 [寒冰箭雨] 2秒施法, 0法力, 45码内 3780-4620 冰霜伤害

    .learn 34449 [水箭雨] 1.5秒施法, 50法力, 35码内 68-82 冰霜伤害
    .learn 59266 [水箭雨] 1.5秒施法, 50法力, 35码内 135-165 冰霜伤害

    .learn 50702 [奥术箭雨] 2.5秒施法, 90法力, 40码内 1700-2300 奥术伤害
    .learn 59212 [奥术箭雨] 2.5秒施法, 90法力, 40码内 3400-4600 奥术伤害

    .learn 56063 [奥爆术] 2秒施法, 120法力, 10码内 1350-1650 奥术伤害, 并击退
    .learn 56067 [奥爆术] 2秒施法, 120法力, 10码内 1800-2200 奥术伤害, 并击退

    .learn 39175 [暗影箭雨] 2秒施法, 160法力, 45码内 1275-1725 暗影伤害
    .learn 56064 [暗影箭雨] 3秒施法, 160法力, 30码内 1575-1925 暗影伤害
    .learn 56065 [暗影箭雨] 3秒施法, 160法力, 30码内 2250-2750 暗影伤害
    .learn 36275 [暗影箭雨] 3秒施法, 160法力, 45码内 1800-2200 暗影伤害
    .learn 38533 [暗影箭雨] 3秒施法, 160法力, 45码内 2925-3575 暗影伤害
    .learn 36275 [暗影箭雨] 1.5秒施法, 3秒CD, 0法力, 35码内 1063-1437 暗影伤害
    .learn 38840 [暗影箭雨] 1.5秒施法, 3秒CD, 0法力, 40码内 2125-2875 暗影伤害

    .learn 29293 [毒液箭雨] 2.5秒施法, 0法力, 30码内 1500-2500 自然伤害, 每5秒造成 238-262 点自然伤害, 持续15秒
    .learn 29325 [毒液箭雨] 瞬发无CD, 无公共CD, 0法力, 50码内 每3秒造成 232-268 点自然伤害, 持续24秒
    .learn 54714 [毒液箭雨] 瞬发无CD, 无公共CD, 0法力, 50码内 每3秒造成 278-322 点自然伤害, 持续24秒

    .learn 36740 [闪电箭雨] 1.5秒施法, 0法力, 35码内 1094-1406 自然伤害
    .learn 38839 [闪电箭雨] 1.5秒施法, 0法力, 40码内 2188-2812 自然伤害

    .learn 36743 [圣光箭雨] 1.5秒施法, 90法力, 35码内 1063-1437 神圣伤害
    .learn 38838 [圣光箭雨] 1.5秒施法, 90法力, 40码内 2125-2875 神圣伤害

    # 瞬发, 无CD, 无公共CD
    .learn 37109 [连珠火球] 瞬发无CD, 无公共CD, 0法力, 45码内 2125-2875 火焰伤害
    .learn 38623 [水箭雨] 瞬发无CD, 无公共CD, 50法力, 35码内 2250-2750 冰霜伤害
    .learn 38335 [水箭雨] 瞬发无CD, 无公共CD, 0法力, 45码内 2775-3225 冰霜伤害
    .learn 37129 [奥术箭雨] 瞬发无CD, 无公共CD, 110法力, 50码内 694-806 奥术伤害
    .learn 40424 [奥术箭雨] 瞬发无CD, 无公共CD, 0法力, 100码内 2775-3225 奥术伤害
    .learn 55851 [暗影箭雨] 瞬发无CD, 无公共CD, 0法力, 30码内 4625-5375 暗影伤害
    .learn 34780 [毒液箭雨] 瞬发无CD, 无公共CD, 0法力, 55码内 1444-1856 暗影伤害, 每2秒造成 289-411 点自然伤害, 持续6秒
    .learn 39340 [毒液箭雨] 瞬发无CD, 无公共CD, 0法力, 55码内 1969-2531 暗影伤害, 每2秒造成 702-988 点自然伤害, 持续6秒

