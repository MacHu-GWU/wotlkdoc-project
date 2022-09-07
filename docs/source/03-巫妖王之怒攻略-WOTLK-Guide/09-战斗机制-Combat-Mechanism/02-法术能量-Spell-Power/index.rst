.. _WLK-Spell-Power:

法术能量 (Spell Power)
===============================================================================
关键词: 法术能量, 法能, 法伤, SP, Spell Power


法伤和治疗效果被统一为法术能量
------------------------------------------------------------------------------
在巫妖王之怒中, 各类法术伤害和治疗效果被统一起来, 所有影响法术伤害和治疗效果的属性都换成为一个新的属性: 法术能量, 或 法术强度, 或简称为 法伤 或 SP.

法术能量属性占用的物品等级和原来 "提高法术伤害和治疗效果" 相同. 法术强度整合了原先的法术伤害, 单系法术伤害与治疗效果三个属性. 随之带来的大量的装备, 附魔, 宝石, Buff 的效果讲被重新定位, 治疗和法系输出装备的区分将模糊化. 法术强度属性与 TBC 的法术伤害属性的数据换算为 1:1, 与 TBC 的治疗效果属性的数值换算约为 1:1.875. 各种装备, 附魔, 宝石, Buff 效果将按照这个比率进行换算. 治疗职业在属性面板中会发现治疗效果数值将会比 TBC 时候低, 但是实际的法术加成不会被减少. 在 WLK 中法系治疗装备的区分只能模糊地从 MP5, 急速, 命中, 暴击等方面区分了. 绝对意义的 "治疗装" 将不复存在. 对于 WLK 之前的装备, 基本按照如下规律进行换算, 并确定属性:

1. 原法术伤害和治疗效果相等的, 统一转换成法术能量, 数值不变.
2. 原治疗效果大于法术伤害的, 将治疗效果数值除以 1.875, 以此数值统一转换成法术能量.


法伤系数
------------------------------------------------------------------------------
所有的法术技能的所造成的实际效果都被统一成了 基础效果 + 法伤 * 系数. 而不同的法术有着不同的系数. 系数越高说明成长性越好. 通常来说有如下规律:

- 系数高: 施法时间长的技能, Dot 技能, 持续治疗技能
- 系数低: 瞬发技能


全职业法伤系数
------------------------------------------------------------------------------
一些缩写:

- DD: Direct Damage, 直接伤害
- DH: Direct Heal, 直接治疗
- DOT: 持续伤害
- HOT: 持续治疗
- Tick: 每一跳


.. _德鲁伊技能法伤系数:

德鲁伊技能法伤系数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/class-icon/07-Druid.png
    :width: 64
    :height: 64

**Healing Abilities**

- [治疗之触 Healing Touch], 161.14% (201.14% with [Empowered Touch]), Patch 3.3.0
- [生命之花 Lifebloom] DH, 38.57%, Patch 3.3.0
- [生命之花 Lifebloom] HoT, 6.53% (per tick) (7.84% with [Empowered Rejuvenation]), Patch 3.3.0
- [回春术 Rejuvenation], 37.6% (per tick, 4 tick) (45.12% with [Empowered Rejuvenation]), Patch 3.3.0
- [愈合 Regrowth] DH, 30%, Patch 3.3.0
- [愈合 Regrowth] HoT, 18.78% (per tick, 7 tick) (22.54% with [Empowered Rejuvenation]), Patch 3.3.0
- [迅捷治愈 Swiftmend] (Rejuvenation), No direct benefit from spellpower, Patch 3.3.0
- [迅捷治愈 Swiftmend] (Regrowth), No direct benefit from spellpower, Patch 3.3.0
- [宁静 Tranquility], 107.43% (per tick) (128.92% with [Empowered Rejuvenation]), Patch 3.3.0
- [野性成长 Wild Growth], 11.51% (per tick, 7 tick) (13.82% with [Empowered Rejuvenation]), Patch 3.3.0
- [滋养 Nourish], 80.57% (100.57% with [Empowered Touch]), Patch 3.3.0

**Damage Abilities**

- [月火术 Moonfire] DD, 14.95%, Patch 3.2.0
- [月火术 Moonfire] DoT, 13.02% (per tick, 4 tick), Patch 3.2.0
- [星火术 Starfire], 100% (120% with [Wrath of Cenarius]), Patch 3.2.0
- [愤怒 Wrath], 57.14% (67.14% with [Wrath of Cenarius]), Patch 3.2.0
- [星落术 Starfall] Per Star, 30%, Patch 3.3.3
- [星落术 Starfall] AoE Per Star, 13%, Patch 3.3.3
- [虫群 Insect Swarm], 20% (per tick, 7 tick), Patch 3.1.0
- [纠缠根须 Entangling Roots] (per tick), 20%, Patch 3.2.0
- [Force of Nature] (per hit), 3.5% (before armor); potentially 50-60 hits during spell duration.
- [飓风 Hurricane], 12.9% (per tick), Patch 3.2.0
- [台风 Typhoon], 19.36%, Patch 3.1.0
- [荆棘术 Thorns] per hit, 3.3%, Patch 3.1.2 (hotfix)

**Feral Abilities (Attack Power Coefficients)**

- [Lacerate] (DD), 1%, Patch 3.1.0
- [Lacerate] (DoT), 1% (per tick), Patch 3.1.0
- [Pounce], 3% (per tick), Patch 3.2.0
- [Swipe], 6.3%, Patch 3.2.0


.. _法师技能伤害系数:

法师技能伤害系数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/class-icon/07-Druid.png
    :width: 64
    :height: 64

**Arcane Abilities**

- [奥术飞弹 Arcane Missiles], 142.86% total, 28.57% per pulse (187.86%/37.57% with [Arcane Empowerment]), Patch 3.3.2
- [奥术冲击 Arcane Blast], 71.43% (80.43% with [Arcane Empowerment]), Patch 3.3.2
- [奥爆术 Arcane Explosion], 21.43%, Patch 3.3.2
- [Mana Shield], 80.53%, Patch 3.0.2
- [Arcane Barrage], 71.43%, Patch 3.3.2

**Fire Abilities**

- [火球术 Fireball] DD, 100.0% (115.0% with [Empowered Fire]), Patch 3.0.2
- [火球术 Fireball] DoT, 0.0%, Patch 3.0.2
- [冲击波 Blast Wave], 19.36%, Patch 3.0.8
- [龙息术 Dragon's Breath], 19.36%, Patch 3.0.8
- [火焰冲击 Fire Blast], 42.86%, Patch 3.0.8
- [烈焰风暴 Flamestrike] DD, 23.57%, Patch 3.0.2
- [烈焰风暴 Flamestrike] DoT, 48.8% (12.2% per tick, 4 tick), Patch 3.0.2
- [炎爆术 Pyroblast] DD, 115.0% (130% with [Empowered Fire]), Patch 3.0.2
- [炎爆术 Pyroblast] DoT, 20.0% (5% per tick), Patch 3.0.2
- [灼烧 Scorch], 42.86%, Patch 3.0.8
- [霜火箭 Frostfire Bolt]DD, 85.71% (100.71% with [Empowered Fire]), Patch 3.0.2
- [霜火箭 Frostfire Bolt]DoT, 0.0%, Patch 3.0.2
- [活体炸弹 Living Bomb] DoT, 80.0% (20.0% per tick, 4 tick), Patch 3.3.0
- [活体炸弹 Living Bomb] DD, 42.86%, Patch 3.3.0

**Frost Abilities**

- [寒冰箭 Frostbolt], 81.43% (91.43% with [Empowered Frostbolt]), Patch 3.3.0
- [冰锥术 Cone of Cold], 20.36%, Patch 3.3.0
- [冰枪术 Ice Lance], 14.29%, Patch 3.3.0
- [冰霜新星 Frost Nova], 19.36%, Patch 3.0.8
- [暴风雪 Blizzard], 114.29% (14.29% per tick, 8 tick), Patch 3.3.0
- [寒冰护体 Ice Barrier], 80.53%, Patch 3.0.2
- [急速冷却 Deep Freeze], 214.3%, Patch 3.3.0

**Summons and pet abilities**

- [Mirror Image], 33% of the mage's spell power, Patch 3.2.0
- [Frost Bolt] (Mirror Image), 30% of the image's spell power (10% of the mage's spell power), Patch 3.2.0[9]
- [Fire Blast] (Mirror Image), 15% of the image's spell power (5% of the mage's spell power), Patch 3.2.0[9]
- [Summon Water Elemental], 33% of the mage's spell power, Patch 3.2.0
- [Water Bolt] (Water Elemental), 83.33% of the elemental's spell power (27.78% of the mage's spell power), Patch 3.2.0[9]


.. _术士技能伤害系数:

术士技能伤害系数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/class-icon/07-Druid.png
    :width: 64
    :height: 64

**Damage over Time Abilities**

- [痛苦诅咒 Curse of Agony], 10.0% per tick (all ticks, 8 tick), 120% (total, unglyphed), 140% (total, [glyphed]) Patch 3.3.2
- [厄运诅咒 Curse of Doom], 200.0%, Patch 3.2.0
- [腐蚀术 Corruption], 20% (per tick, 6 tick) (26% with [Empowered Corruption]) (31% with [Empowered Corruption] & [Everlasting Affliction]) 120.0% Total (156% with [Empowered Corruption]) (186% with [Empowered Corruption] & [Everlasting Affliction]) Patch 3.3.2
- [不稳定的痛苦 Unstable Affliction] (periodic damage), 20% (per tick, 5 tick) (25% with [Everlasting Affliction]) 100.0% Total (125% with [Everlasting Affliction]) Patch 3.3.3
- [不稳定的痛苦 Unstable Affliction] (Dispelled), 180%, Patch 3.3.3

**Hybrid Abilities**

- [献祭 Immolate] (DoT), 20.0% (per tick, 5 tick) (100% total), Patch 3.2.0
- [献祭 Immolate] (DD), 20.0%, Patch 3.2.0
- [献祭 Immolate] (total), 120%, Patch 3.2.0
- [腐蚀之种 Seed of Corruption] (DoT component), 25.0% (per tick), Patch 3.2.0
- [腐蚀之种 Seed of Corruption] (DD component), 21.29%, Patch 3.2.0
- [暗影烈焰 Shadowflame] (DoT component), 6.67% (per tick, 4 tick) (26.68% total), Patch 3.2.0
- [暗影烈焰 Shadowflame] (DD component), 10.64%, Patch 3.2.0
- [暗影烈焰 Shadowflame] (total), 37.74%, Patch 3.2.0

**Direct Damage Abilities**

- [暗影箭 Shadow Bolt], 85.71% (102.85% with [Shadow and Flame]), Patch 3.3.3
- [灵魂之火 Soul Fire], 115%, Patch 3.2.0
- [灼热之痛 Searing Pain], 42.86%, Patch 3.3.0
- [暗影灼烧 Shadowburn], 42.86% (51.42% with [Shadow and Flame]), Patch 3.3.3
- [烧尽 Incinerate] (unconditional damage), 71.43% (85.71% with [Shadow and Flame]), Patch 3.3.3
- [点燃 Conflagrate], No direct benefit from spell power., Patch 3.3.0
- [混乱箭 Chaos Bolt], 71.42% (85.71% with [Shadow and Flame]), Patch 3.3.3
- [死亡缠绕 Death Coil], 21.43%, Patch 3.3.0
- [鬼影重重 Haunt], 42.86%, Patch 3.3.0
- [暗影之怒  Shadowfury], 19.36%, Patch 3.3.0
- [地狱火 Inferno], 100%, Patch 3.3.3

**Channeled Abilities**

- [Drain Life], 14.30% (per tick, 5 tick), Patch 3.2.0
- [Drain Mana], 0.0%
- [Drain Soul], 42.90% (per tick, 5 tick), Patch 3.2.0
- [Health Funnel] (healing), 54.8% per tick (548% total), Patch 3.3.0a
- [Hellfire] (to enemies), 14.3% (per tick, 8 tick), Patch 3.2.0
- [Hellfire] (to self), 9.49% (per tick, 8 tick), Patch 3.2.0
- [Rain of Fire], 33.00% (per tick, 8 tick), Patch 3.3.0

**Other Abilities**

- [Dark Pact] (mana drained), 96.0%
- [Life Tap], 50% (for mana gained, health cost is unmodified), Patch 3.3.3
- [Shadow Ward], 80.7%[note 2]
- [Metamorphosis] Abilities
- [Immolation Aura], ~214.5% (~14.3% per tick) (243.23% (16.22% per tick) after Metamorphosis' 20% damage bonus), 3.2.2
- [Shadow Cleave], ~21.3% (~25.6% after Metamorphosis' 20% damage bonus), 3.2.2

**Warlock minion**

All values are before the effects of talents, glyphs and buffs.

Source: rawr 2.2.19 source code [3]

- Felhunter, Auto-attack (per second), 3.25% (0.57/17.5), 5.71% (1/17.5) of minion attack power, 3.3.3
- Succubus, Auto-attack (per second), 4.28% (0.57/13.33), 7.5% (1/13.33) of minion attack power, 3.3.3
- Voidwalker, Auto-attack (per second), 4.9% (0.798/16.28)[note 3], 6.14% (1/16.28) of minion attack power, 3.3.3
- Felguard, Auto-attack (per second), 4.07% (0.57/14), 7.14% (1/14) of minion attack power, 3.3.3
- Imp, [Firebolt], 10.71%, 71.42%, 3.3.3
- Imp, [Fire Shield] (per hit), 0%, 0%, 3.3.3
- Voidwalker, [Consume Shadows] (healing), 0%, 0%, 3.3.3
- Voidwalker, [Sacrifice] (damage absorbed), 0%, 0%, 3.3.3
- Voidwalker, [Suffering] (threat), ?, ?, Never
- Voidwalker, [Torment] (threat), ?, ?, Never
- Succubus, [Lash of Pain], 6.43%, 42.90%, 3.3.3
- Felhunter, [Devour Magic] (healing), 0%, 0%, 3.3.3
- Felhunter, [Shadow Bite], 6.43%, 42.90%, 3.3.3
- Felguard, [Anguish] (threat), ?, ?, Never
- Felguard, [Cleave], ~8.14% (0.57/7), n/a (~14.29% (1/7) of attack power), ?
- Felguard, [Intercept], ~1.6%, n/a (~2.8% of attack power), 3.2.2
- Infernal, [Immolation], 20.25% (per tick), 135% (per tick), 3.3.3
- Doomguard, [Rain of Fire], 6% (1.5% per tick), 40% (10% per tick), 3.3.3
- Doomguard, [War Stomp], 0%, 0%, 3.3.3


.. _牧师技能伤害系数:

牧师技能伤害系数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/class-icon/07-Druid.png
    :width: 64
    :height: 64

**Healing Abilities**

- [联结治疗 Binding Heal], 80.57% (100.57% with [Empowered Healing]), Patch 3.2.0
- [治疗之环 Circle of Healing], 40.29%, Patch 3.2.0
- [绝望祷言 Desperate Prayer], 80.57%, Patch 3.2.0
- [快速治疗 Flash Heal], 80.57% (100.57% with [Empowered Healing]), Patch 3.2.0
- [超级治疗术 Greater Heal], 161.14% (201.14% with [Empowered Healing]), Patch 3.2.0
- [神圣新星 Holy Nova] (Healing), 30.35%, Patch 3.2.0
- [苦修 Penance] (Healing), 53,62% (per tick, 160,86% total), Patch 3.3.0
- [真言术盾 Power Word: Shield], 80.57%, Patch 3.0.8
- [治疗祷言 Prayer of Healing], 52.6%, Patch 3.2.0
- [愈合祷言 Prayer of Mending] (per charge), 80.57%, Patch 3.2.0
- [恢复 Renew], 37.6% (per tick, 5 tick; 40.6% with [Empowered Renew] per tick), Patch 3.2.0

**Offensive Abilities**

- [暗言术痛 Shadow Word: Pain], 18.33% (per tick; totaling 110%), Patch 3.2.0
- [暗言术死 Shadow Word: Death], 42.86%, Patch 3.2.0
- [精神震爆 Mind Blast], 42.86% (57.86% with [Misery]), Patch 3.2.0
- [精神鞭笞 Mind Flay], 25.70% (per tick, 3 tick; totaling 77.1%); 30.7% per tick (total 92.1%) with [Misery]), Patch 3.2.0
- [精神灼烧 Mind Sear], 28.57% (per tick, 5 tick; totaling 142.86%); 31.57% per tick (total 157.86%) with [Misery]), Patch 3.2.0
- [噬灵瘟疫 Devouring Plague], 20.00% (per tick, 8 tick; 160% total), Patch 3.2.0
- [吸血鬼之触 Vampiric Touch], 40.0% (per tick; totaling 200%), Patch 3.2.0
- [吸血鬼之触 Vampiric Touch] (Dispelled), 120%
- [神圣之火 Holy Fire] DD, 57.5%, Patch 3.2.0
- [神圣之火 Holy Fire] DoT, 5.29% (per tick; 18.5% total), Patch 3.2.0
- [神圣新星 Holy Nova] (Damage), 21.43%, Patch 3.2.0
- [法力燃烧 Mana Burn], 0.0%
- [Shadowfiend], 35.68% (per hit) (356.8%...392.5% over the total duration), Patch 3.2.0
- [苦修 Penance] (Damage), 19.05% (per tick, 57.14% total), Patch 3.3.0
- [惩击 Smite], 71.43%, Patch 3.2.0


.. _萨满技能伤害系数:

萨满技能伤害系数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/class-icon/05-Shaman.png
    :width: 64
    :height: 64

**Healing Abilities**

- [治疗波 Healing Wave], 161.14% (181.14% with [Tidal Waves]), Patch 3.3.0
- [次级治疗波 Lesser Healing Wave], 80.57% (90.57% with [Tidal Waves]), Patch 3.3.0
- [治疗链 Chain Heal], 263.19% (134.28% + 80.57% + 48.34% on each "jump", respectively) 292.19% glyphed (29% on forth "jump".) Patch 3.3.0
- [大地之盾 Earth Shield], 13.43% per charge, Patch 3.0.2
- [治疗之泉图腾 Healing Stream Totem] (per tick), 4.45%, Patch 3.3.0
- [激流 Riptide], 134.2% (40.2% direct, 18.8% per tick * 5), Patch 3.3.0

**Offensive Abilities**

- [闪电箭 Lightning Bolt], 71.43% (91.43% with [Shamanism]), Patch 3.3.0
- [闪电链 Chain Lightning], 125.14% (57.14% + 40% + 28% on each "jump", respectively) 145.14% with [Shamanism]; 164.74% glyphed with Shamanism (19.6% on forth "jump".) Patch 3.3.0
- [火焰震击 Flame Shock] DD, 21.43%, Patch 3.3.0
- [火焰震击 Flame Shock] DoT, 10.00% per tick, 6 tick; totaling 60.00%, Patch 3.3.0
- [冰霜震击 Frost Shock], 38.58%, Patch 3.0.3
- [大地震击 Earth Shock], 38.58%, Patch 3.0.3
- [火焰新星图腾 Fire Nova Totem], 21.42%, Patch 3.0.3
- [闪电盾 Lightning Shield], 33.33% per charge, Patch 3.0.2
- [冰霜武器 Frostbrand Weapon] (per hit), 10%
- [火舌图腾 Flametongue Weapon] (per hit), 10%
- [熔岩爆裂 Lava Burst], 57.14% (82.14% with [Shamanism]; 92.14% with [Glyph of Lava] and [Shamanism]), Patch 3.3.0
- [熔岩爆发图腾 Magma Totem], 10% per tick, Patch 3.0.8
- [灼热图腾 Searing Totem], 16.67% per tick, Patch 3.0.3


.. _圣骑士技能伤害系数:

圣骑士技能伤害系数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: /_static/image/class-icon/02-Paladin.png
    :width: 64
    :height: 64

**Healing Abilities**

- [圣光闪现 Flash of Light], 100%, Patch 3.3
- [圣光术 Holy Light], 166%, Patch 3.3
- [神圣冲击 Holy Shock], 80.57%, Patch 3.2.2
- [圣洁之盾 Sacred Shield], 75.00%, Patch 3.2.2

**Offensive Abilities**

- [Avenger's Shield], 7.0%, 7.0%, ?
- [Hand of Reckoning], 0%, 50%, Patch 3.3
- [Consecration], 32% (4% per second), 32% (4% per second), Patch 3.3
- [Crusader Strike], 0%, from weapon, Patch 3.3
- [Divine Storm], 0%, from weapon, Patch 3.3
- [Exorcism], 15.0%, 15.0%, Patch 3.3
- [Hammer of Wrath], 15.0%, 15.0%, Patch 3.3
- [Holy Shield] (per block), 9.0%, 5.6%, Patch 3.0.9
- [Holy Shock], 42.86%, 0.0%, Patch 3.0.9
- [Holy Wrath], 7.0%, 7.0%, ?
- [Retribution Aura], 3.3%, 0%, Patch 3.3
- [Seal of Command] (on hit), 0%, 5%, Patch 3.3
- [Seal of Command] (judgement), 14%, 11.5%, Patch 3.3
- [Seal of Corruption] (DOT), 33% (6.6% per tick), 63% (12.6% per tick), Patch 3.3
- [Seal of Corruption] (judgement), 24%, 15%, Patch 3.3
- [Seal of Justice] (chance of stun on hit), , , Patch 3.3
- [Seal of Justice] (judgement), 27.0%, 17.5%, Patch 3.3
- [Seal of Wisdom] (mana on hit), , , Patch 3.3
- [Seal of Wisdom] (judgement), 27.0%, 17.5%, Patch 3.3
- [Seal of Light] (heal on hit), 15.0%, 15.0%, Patch 3.3
- [Seal of Light] (judgement), 27.0%, 17.5%, Patch 3.3
- [Seal of Righteousness] (per second), 9.5%, 4.5%, Patch 3.3
- [Seal of Righteousness] (judgement), 35.5%, 22.5%, Patch 3.3
- [Seal of Vengeance] (DOT), 33% (6.6% per tick), 63% (12.6% per tick), Patch 3.3
- [Seal of Vengeance] (judgement), 24%, 15%, Patch 3.3
- [Shield of Righteousness], 0.0%, 0.0%, Patch 3.0.8


参考资料
------------------------------------------------------------------------------
- https://wowwiki-archive.fandom.com/wiki/Spell_power_coefficient
