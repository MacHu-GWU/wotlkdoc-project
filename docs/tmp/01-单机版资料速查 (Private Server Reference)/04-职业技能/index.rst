.. _职业技能代码GM命令:

职业技能代码 (Class Spell)
===============================================================================

.. image:: /_static/images/class-icon/01-Warrior.png
    :height: 128px
    :width: 128px
    :target: 战士技能ID_
.. image:: /_static/images/class-icon/02-Paladin.png
    :height: 128px
    :width: 128px
    :target: 圣骑士技能ID_
.. image:: /_static/images/class-icon/03-Hunter.png
    :height: 128px
    :width: 128px
    :target: 猎人技能ID_
.. image:: /_static/images/class-icon/04-Shaman.png
    :height: 128px
    :width: 128px
    :target: 萨满祭司技能ID_
.. image:: /_static/images/class-icon/05-Rogue.png
    :height: 128px
    :width: 128px
    :target: 盗贼技能ID_
.. image:: /_static/images/class-icon/06-Druid.png
    :height: 128px
    :width: 128px
    :target: 德鲁伊技能ID_
.. image:: /_static/images/class-icon/07-Mage.png
    :height: 128px
    :width: 128px
    :target: 法师技能ID_
.. image:: /_static/images/class-icon/08-Warlock.png
    :height: 128px
    :width: 128px
    :target: 术士技能ID_
.. image:: /_static/images/class-icon/09-Priest.png
    :height: 128px
    :width: 128px
    :target: 牧师技能ID_
.. image:: /_static/images/class-icon/10-Death-Knight.png
    :height: 128px
    :width: 128px
    :target: 死亡骑士技能ID_


如果你在游戏中看到一个技能, 但不知道这个技能的ID, 那么你有以下三种办法可以获得这个技能的ID。

1. 使用 ``.lookup spell <spell_name>`` GM命令, 通过技能的英文名搜索。比如搜索火球术就要 ``.lookup spell firebolt``。然后根据技能描述, 确定是不是你想要的那个技能。
2. 如果这个技能在技能栏中, 又或有一个Buff图标, **那么推荐安装SpellID插件**, 只要你能看到技能的图片, 既可显示技能ID。
3. 如果这个技能是一个职业技能或天赋技能, 而你的技能书中没有, 那么可以打开 ``ItemDB`` 插件, 打开 ``PeriodicTable - ClassSpell``, 里面有所有职业的技能书中出现的技能.
4. 在 https://wotlk.evowow.com/ 或 https://wotlk-twinhead.twinstar.cz/ 数据库网站上通过技能分类手动搜索。

下面列出了所有职业的主要技能的ID (未一一验证, 请以 #2, #3, #4 的查询结果为准)。

.. _战士技能ID:

战士 (Warrior)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/Warrior.png
    :height: 128px
    :width: 128px


武器 (Arm)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 战斗姿态 (Battle Stance), 2457
- 英勇打击 (Heroic Strike), 30324
- 撕裂 (Rend), 25208
- 雷霆一击 (Thunder Clap), 47502
- 冲锋 (Charge), 11578
- 致死打击 (Mortal Strike), 30330
- 英勇投掷 (Heroic Throw), 57755
- 惩戒痛击 (Mocking Blow), 694
- 反击风暴 (Retaliation), 20230
- 断筋 (Hamstring), 1715
- 姿态掌握 (Stance Mastery), 12678


狂暴 (Fury)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 狂暴姿态 (Berserker Stance), 2458
- 拦截 (Intercept), 20252
- 刺耳嚎叫 (Piercing Howl), 12323
- 战斗怒吼 (Battle Shout), 2048
- 挫志怒吼 (Demoralizing Shout), 25203
- 挑战怒吼 (Challenging Shout), 1161
- 破胆怒吼 (Intimidating Shout), 5246
- 命令怒吼 (Commanding Shout), 469
- 血性狂暴 (Bloodrage), 2687
- 狂暴之怒 (Berserker Rage), 18499
- 鲁莽 (Recklessness), 1719
- 拳击 (Pummel), 6552
- 猛击 (Slam), 25242
- 旋风斩 (Whirlwind), 1680
- 顺劈斩 (Cleave), 25231
- 乘胜追击 (Victory Rush), 34428
- 斩杀 (Execute), 25236
- 嗜血 (Bloodthirst), 30335


防护 (Protection)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 防御姿态 (Defensive Stance), 71
- 嘲讽 (Taunt), 355
- 破甲攻击 (Sunder Armor), 25225
- 盾牌格挡 (Shield Block), 2565
- 复仇 (Revenge), 30357
- 盾击 (Shield Bash), 29704
- 盾牌猛击 (Shield Slam), 30356
- 缴械 (Disarm), 676
- 盾墙 (Shield Wall), 871
- 震荡猛击 (Concussion Blow), 12809
- 援护 (Intervene), 3411
- 冲击波 (Shockwave), 46968
- 毁灭打击 (Devastate), 30022
- 法术反射 (Spell Reflection), 23920


.. _圣骑士技能ID:

圣骑士 (Paladin)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/Paladin.png
    :height: 128px
    :width: 128px


祝福 (Blessing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 力量祝福 (Blessing of Might), 27140
- 强效力量祝福 (Greater Blessing of Might) 27141
- 智慧祝福 (Blessing of Wisdom), 27142
- 强效智慧祝福 (Greater Blessing of Wisdom) 27143
- 王者祝福 (Blessing of Kings), 20217
- 强效王者祝福 (Greater Blessing of Kings), 25898
- 庇护祝福 (Blessing of Sanctuary), 67480
- 强效庇护祝福 (Greater Blessing of Sanctuary), 25899


光环 (Aura)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 虔诚光环 (Devotion Aura), 48942
- 火焰抗性光环 (Fire Resistance Aura), 27153
- 冰霜抗性光环 (Frost Resistance Aura), 27152
- 暗影抗性光环 (Shadow Resistance Aura), 27151
- 惩戒光环 (Retribution Aura), 27150
- 专注光环 (Concentration Aura) 19746
- 十字军光环 (Crusader Aura), 32223


圣印 (Seal)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 正义圣印 (Seal of Righteousness), 21084
- 光明圣印 (Seal of Light), 20165
- 公正圣印 (Seal of Justice), 20164
- 智慧圣印 (Seal of Wisdom), 20166
- 命令圣印 (Seal of Command), 20375
- 殉难圣印 (Seal of the Martyr), 53720
- 复仇圣印 (Seal of Vengeance), 31801


审判 (Judgement)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 光明审判 (Judgement of Light), 20271
- 智慧审判 (Judgement of Wisdom), 53408
- 公正审判 (Judgement of Justice), 53407


惩戒 (Retribution)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 奉献 (Consecration), 48819
- 复仇之怒 (Avenging Wrath), 31884
- 愤怒之锤 (Hammer of Wrath), 27180
- 战争艺术 (The Art of War), 59578
- 神性风暴 (Divine Storm), 53385
- 十字军打击 (Crusader Strike), 35395
- 忏悔 (Repentance), 20066


防护 (Protection)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 制裁之锤 (Hammer of Justice), 10308
- 圣盾术 (Divine Shield), 642
- 圣佑术 (Divine Protection), 498
- 自由之手 (Hand of Freedom), 1044
- 牺牲之手 (Hand of Sacrifice), 6940
- 保护之手 (Hand of Protection), 10278
- 拯救之手 (Hand of Salvation), 1038
- 神圣之盾 (Holy Shield), 27179
- 复仇者之盾 (Avenger's Shield), 32700
- 正义之锤 (Hammer of the Righteous), 53595
- 神圣干涉 (Divine Intervention), 19752
- 正义之怒 (Righteous Fury), 25780
- 正义防御 (Righteous Defense), 31789
- 灵魂协调 (Spiritual Attunement), 33776


神圣 (Holy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 神圣震击 (Holy Shock), 33074
- 神圣愤怒 (Holy Wrath), 27139
- 圣光术 (Holy Light), 27136
- 圣光闪现 (Flash of Light), 27137
- 圣疗术 (Lay on Hands), 27154
- 神性祈求 (Divine Plea), 54428
- 圣光信标 (Light's Beacon), 53651
- 圣洁之盾 (Sacred Shield), 53601
- 救赎 (Redemption), 20773
- 清洁术 (Cleanse), 498
- 纯净术 (Purify), 1152
- 驱邪术 (Exorcism), 27138
- 超度邪恶 (Turn Evil), 10326
- 感知亡灵 (Sense Undead), 5502


.. _猎人技能ID:

猎人 (Hunter)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/Hunter.png
    :height: 128px
    :width: 128px

- 瞄准射击 (skillname), 27065
- 翼龙钉刺 (skillname), 27069
- 误导 (skillname), 34477
- 猫鼬撕咬 (skillname), 36916
- 爆炸射击 (skillname), 60051
- 奥术射击 (skillname), 27019
- 雄鹰守护 (skillname), 27044
- 野性守护 (skillname), 27045
- 治疗宠物 (skillname), 27046
- 毒蛇陷阱 (skillname), 34600
- 毒蛇钉刺 (skillname), 27016
- 多重射击 (skillname), 27021
- 乱射 (skillname), 27022
- 蝰蛇钉刺 (skillname), 27018
- 反击 (skillname), 27067
- 杀戮命令 (skillname), 34026
- 献祭陷阱 (skillname), 27023
- 猛禽一击 (skillname), 27014
- 稳固射击 (skillname), 34120
- 爆炸陷阱 (skillname), 27025
- 冰冻陷阱 (skillname), 14311
- 威慑 (skillname), 19263
- 宁神射击 (skillname), 19801
- 瞄准射击 (skillname), 20904
- 翼龙钉刺 (skillname), 24135
- 多重射击 (skillname), 25294
- 冰冻之箭 (skillname), 60202
- 猫鼬撕咬 (skillname), 14271
- 猎人印记 (skillname), 14325
- 献祭陷阱 (skillname), 14305
- 追踪龙类 (skillname), 19879
- 豹群守护 (skillname), 13159
- 追踪巨人 (skillname), 19882
- 照明弹 (skillname), 1543
- 追踪恶魔 (skillname), 19878
- 假死 (skillname), 5384
- 野兽守护 (skillname), 13161
- 恐吓野兽 (skillname), 14326
- 急速射击 (skillname), 3045
- 追踪元素生物 (skillname), 19880
- 野兽知识 (skillname), 1462
- 追踪隐藏生物 (skillname), 19885
- 毒蝎钉刺 (skillname), 3043
- 逃脱 (skillname), 781
- 猎豹守护 (skillname), 5118
- 蝰蛇守护 (skillname), 34074
- 追踪亡灵 (skillname), 19884
- 野兽之眼 (skillname), 1002
- 鹰眼术 (skillname), 6197
- 摔绊 (skillname), 2974
- 扰乱射击 (skillname), 20736
- 召唤宠物 (skillname), 883
- 复活宠物 (skillname), 882
- 驯服野兽 (skillname), 1515
- 解散野兽 (skillname), 2641
- 喂养宠物 (skillname), 6991
- 追踪人型生物 (skillname), 19883
- 震荡射击 (skillname), 5116
- 灵猴守护 (skillname), 13163
- 自动射击 (skillname), 75
- 追踪野兽 (skillname), 1494


野兽掌握 (Beast Mastery)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


射击 (Marksmanship)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


生存 (Survival)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _萨满祭司技能ID:

萨满祭司 (Shaman)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/Shaman.png
    :height: 128px
    :width: 128px

::

    # 可替代所有的4种图腾使用
    .add 46978 [大地之环图腾]

元素护盾:

- 闪电之盾: 49281
- 水之护盾: 57960
- 大地之盾: 49284

震击:

- 烈焰震击: 49233, 造成火焰伤害, 以及持续伤害
- 冰霜震击: 49236, 造成冰霜伤害, 降低移动速度
- 大地震击: 49231, 造成自然伤害, 降低近战攻击速度
- 削风术: 57994, 打断目标施法

元素战斗伤害性法术:

- 闪电箭: 49238
- 闪电链: 49271
- 熔岩爆发: 60043
- 雷霆风暴: 59159

增强肉搏伤害技能:

- 熔岩打击: 60103, 用副手武器造成伤害
- 风暴打击: 17364, 用主副武器同事造成伤害, 并提高下4次自然法术的伤害

治疗法术:

- 次级治疗波: 49276
- 治疗波: 49273
- 治疗链: 55459
- 激流: 61301, 瞬发直接治疗+HOT治疗, 并大幅提高下一个普通治疗技能的效果

辅助法术:

- 先祖之魂 (skillname), 20776
- 复生 (skillname), 20608
- 净化术: 8012, 移除敌人身上2个有益法术
- 星界传送 (skillname), 556

- 视界术 (skillname), 6196
- 水上行走 (skillname), 546
- 水下呼吸 (skillname), 131
- 幽魂之狼 (skillname), 2645

- 祛病术 (skillname), 2870
- 消毒术 (skillname), 526

元素武器:

- 石化武器 (skillname), 10399
- 火舌武器 (skillname), 25489
- 冰封武器 (skillname), 25500
- 风怒武器 (skillname), 25505
- 大地生命武器 (skillname), 51993

控制技能:

- 妖术: 51514

火焰图腾:

- 火焰新星图腾 (skillname), 25547
- 灼热图腾 (skillname), 25533
- 火舌图腾 (skillname), 25557
- 熔岩图腾 (skillname), 25552
- 抗寒图腾 (skillname), 25560
- 火元素图腾 (skillname), 2894
- 愤怒图腾 (skillname), 30706

水之图腾:

- 治疗之泉图腾 (skillname), 25567
- 法力之泉图腾 (skillname), 25570
- 抗火图腾 (skillname), 25563
- 祛病图腾 (skillname), 8170
- 清毒图腾 (skillname), 8166
- 法力之泉图腾 (skillname), 58777

大地图腾:

- 石肤图腾 (skillname), 25509
- 石爪图腾 (skillname), 25525
- 地缚图腾 (skillname), 2484
- 大地之力图腾 (skillname), 25528
- 岗哨图腾 (skillname), 6495
- 战栗图腾 (skillname), 8184
- 土元素图腾 (skillname), 2062

风之图腾:

- 风怒图腾 (skillname), 8512
- 风惩图腾 (skillname), 3738
- 根基图腾 (skillname), 8177
- 空气之怒图腾 (skillname), 3738
- 自然抗性图腾 (skillname), 25574
- 天怒图腾 (skillname), 57721

批量图腾:

- 远古呼唤: 66844
- 先祖呼唤: 66843
- 元素呼唤: 66842
- 图腾召回: 36936

长CD法术:

- 嗜血: 2825
- 英勇: 32182
- 潮汐之力: 55198, 使治疗法术暴击率提高60%, 可暴击3次
- 元素掌握: 16166, 使下一个法术瞬发, 并提高15%施法速度, 持续15秒
- 自然迅捷: 16188, 使下一个法术瞬发


.. include:: ./Rogue.rst

.. include:: ./Druid.rst

.. include:: ./Mage.rst

.. include:: ./Warlock.rst

.. include:: ./Priest.rst

.. include:: ./DeathKnight.rst

.. _死亡骑士技能ID:

死亡骑士 (Death Knight)
-------------------------------------------------------------------------------
.. image:: /_static/images/class-icon/Death-Knight.png
    :height: 128px
    :width: 128px



鲜血 (Blood)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



冰霜 (Frost)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



邪恶 (Unholy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


