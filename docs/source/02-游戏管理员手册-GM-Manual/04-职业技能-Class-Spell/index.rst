.. _职业技能GM命令:

职业技能 (Class Spell)
===============================================================================
.. image:: /_static/image/class-icon/01-Warrior.png
    :height: 128px
    :width: 128px
    :target: 战士技能ID_

.. image:: /_static/image/class-icon/02-Paladin.png
    :height: 128px
    :width: 128px
    :target: 圣骑士技能ID_

.. image:: /_static/image/class-icon/03-DeathKnight.png
    :height: 128px
    :width: 128px
    :target: 死亡骑士技能ID_

.. image:: /_static/image/class-icon/04-Hunter.png
    :height: 128px
    :width: 128px
    :target: 猎人技能ID_

.. image:: /_static/image/class-icon/05-Shaman.png
    :height: 128px
    :width: 128px
    :target: 萨满祭司技能ID_

.. image:: /_static/image/class-icon/06-Rogue.png
    :height: 128px
    :width: 128px
    :target: 盗贼技能ID_

.. image:: /_static/image/class-icon/07-Druid.png
    :height: 128px
    :width: 128px
    :target: 德鲁伊技能ID_

.. image:: /_static/image/class-icon/08-Mage.png
    :height: 128px
    :width: 128px
    :target: 法师技能ID_

.. image:: /_static/image/class-icon/09-Warlock.png
    :height: 128px
    :width: 128px
    :target: 术士技能ID_

.. image:: /_static/image/class-icon/10-Priest.png
    :height: 128px
    :width: 128px
    :target: 牧师技能ID_


如果你在游戏中看到一个技能, 但不知道这个技能的ID, 那么你有以下三种办法可以获得这个技能的ID。

1. 使用 ``.lookup spell <spell_name>`` GM命令, 通过技能的英文名搜索。比如搜索火球术就要 ``.lookup spell firebolt``。然后根据技能描述, 确定是不是你想要的那个技能。
2. 如果这个技能在技能栏中, 又或有一个Buff图标, **那么推荐安装SpellID插件**, 只要你能看到技能的图片, 既可显示技能ID。
3. 如果这个技能是一个职业技能或天赋技能, 而你的技能书中没有, 那么可以打开 ``ItemDB`` 插件, 打开 ``PeriodicTable - ClassSpell``, 里面有所有职业的技能书中出现的技能.
4. 在 https://wotlk.evowow.com/ 或 https://wotlk-twinhead.twinstar.cz/ 数据库网站上通过技能分类手动搜索。

下面列出了所有职业的主要技能的ID (未一一验证, 请以 #2, #3, #4 的查询结果为准)。

.. _战士技能ID:

战士 (Warrior)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/01-Warrior.png
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
.. image:: /_static/image/class-icon/02-Paladin.png
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


.. _死亡骑士技能ID:

死亡骑士 (Death Knight)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/03-DeathKnight.png
    :height: 128px
    :width: 128px



鲜血 (Blood)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



冰霜 (Frost)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



邪恶 (Unholy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _猎人技能ID:

猎人 (Hunter)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/04-Hunter.png
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
.. image:: /_static/image/class-icon/05-Shaman.png
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


.. _盗贼技能ID:

盗贼 (Rogue)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/06-Rogue.png
    :height: 128px
    :width: 128px

潜行技:

- 潜行: 1784
- 闷棍: 51724
- 扰乱: 1725
- 偷窃: 921
- 解除陷阱: 1842

潜行攻击技:

- 偷袭: 1833
- 伏击: 48691
- 绞喉: 48676

攒星技:

- 凿击: 1776, 使敌人迷惑4秒
- 邪恶攻击: 48638, 造成武器伤害
- 背刺: 48657
- 毒袭: 5938, 用副手武器上毒
- 鬼魅攻击: 14278, 提高15%躲闪
- 毁伤: 48666, 用双匕首攻击
- 出血: 48660, 造成武器伤害, 并使目标收到更高的物理伤害

终结技:

- 剔骨: 48668, 造成直接伤害
- 割裂: 48672, 造成流血伤害
- 切割: 6774, 提高攻击速度
- 肾击: 8643, 使目标昏迷
- 毒伤: 57993, 造成毒药伤害
- 致命投掷: 48674, 造成伤害, 并使目标减速
- 破甲: 8647

其他技能:

- 脚踢: 1766
- 佯攻: 48659
- 拆卸: 51722, 拆卸武器和盾牌

AOE:

- 刀扇: 51723

长CD, PvP技能:

- 消失: 26889, 强制进入潜行状态
- 疾跑: 11305, 大幅提高移动速度
- 闪避: 26669, 大幅提高闪避
- 致盲: 2094, 使目标迷惑10秒
- 冷血: 14177, 下一次技能必暴
- 预谋: 14183, 立刻为目标增加2个连击点
- 预备: 14185, 重置所有长CD技能冷却
- 暗影斗篷: 31224, 解除不良状态, 并在5秒内提高90%魔法抗性
- 暗影之舞: 51713, 可以在非潜行状态下使用需要潜行的技能
- 暗影步: 36554, 传送到目标身后
- Overkill: 58426, 潜行和解除潜行后的20秒内, 能量恢复速度提高30%

爆发类技能:

- 冲动: 13750, 能量恢复速度提高100%
- 剑刃乱舞: 13877, 提高攻击速度, 并可以额外攻击一个附近的敌人
- 杀戮盛宴: 51690, 每0.5秒对敌人用双手武器造成攻击, 并且期间伤害提高20%
- 血之饥渴: 51662, 提高5%所有伤害

被动技能:

- 安全降落: 1860
- 侦测陷阱: 2836


.. _德鲁伊技能ID:

德鲁伊 (Druid)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/07-Druid.png
    :height: 128px
    :width: 128px


平衡 (Balance)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
单体:

- 月火术 (skillname), 48463
- 愤怒 (skillname), 48461
- 星火术 (skillname), 48465
- 虫群 (skillname), 48468
- 精灵之火 (skillname), 770
- 星辰坠落 (skillname), 53201

AOE:

- 飓风 (skillname), 48467
- 旋风 (skillname), 61384

控制:

- 纠缠根须 (skillname), 53308
- 休眠 (skillname), 18658
- 安抚动物 (skillname), 26995
- 龙卷风 (skillname), 33786

大招:

- 激活 (skillname), 29166
- 树皮术 (skillname), 22812
- 自然之握 (skillname), 53312


野性战斗 (Feral Combat)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**变形**:

- 熊形态 (skillname), 5487
- 巨熊形态 (skillname), 9634
- 猎豹形态 (skillname), 768
- 水栖形态 (skillname), 1066
- 旅行形态 (skillname), 783
- 飞行形态 (skillname), 33943
- 迅捷飞行形态 (skillname), 40120
- 枭兽形态 (skillname), 24858
- 生命之树形态 (skillname), 33891
- 精灵之火野性 (skillname), 27011

**熊形态**:

- 低吼 (skillname), 6795
- 挑战咆哮 (skillname), 5209

- 重殴(类似英勇打击) (skillname), 48480
- 割伤(仇恨技) (skillname), 33745
- 裂伤-熊 (skillname), 33987
- 猛击(昏迷技) (skillname), 5211
- 横扫-熊 (skillname), 48562
- 狂暴回复 (skillname), 22842
- 挫志咆哮 (skillname), 26998

**豹形态**:

潜行技:

- 潜行 (skillname), 5215
- 突袭(类似偷袭) (skillname), 49803
- 毁灭(类似伏击) (skillname), 48579

攒星技:

- 斜掠(类似割裂) (skillname), 48574
- 爪击(类似邪恶攻击) (skillname), 48570
- 撕碎(类似背刺) (skillname), 48572
- 裂伤-豹 (skillname), 33983

终结技:

- 割裂(类似割裂) (skillname), 49800
- 凶猛撕咬(类似剔骨) (skillname), 48577
- 野蛮咆哮 (skillname), 52610
- 割碎(类似肾击) (skillname), 49802

其他技能:

- 横扫-豹 (skillname), 62078
- 畏缩 (skillname), 31709
- 豹之优雅 (skillname), 20719
- 畏缩 (skillname), 27004
- 急奔 (skillname), 33357
- 猛虎之怒 (skillname), 9846
- 追踪人型生物 (skillname), 5225


恢复 (Restoration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
HOT:

- 回春术 (skillname), 48441
- 生命绽放 (skillname), 48451
- 野性成长 (skillname), 53251

读条治疗:

- 愈合 (skillname), 48443
- 治疗之触 (skillname), 48378
- 滋养 (skillname), 50464

瞬发治疗:

- 迅捷治愈 (skillname), 18562

Buff:

- 野性印记 (skillname), 48469
- 野性赐福 (skillname), 48470
- 自然之握 (skillname), 53312
- 荆棘术 (skillname), 53307

复活:

- 起死回生(复活) (skillname), 50764
- 复生(战斗复活) (skillname), 26994

驱散:

- 驱毒术 (skillname), 2893
- 消毒术 (skillname), 8946
- 解除诅咒 (skillname), 2782

大招:

- 宁静 (skillname), 48447


.. _法师技能ID:

法师 (Mage)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/08-Mage.png
    :height: 128px
    :width: 128px

.. contents::
    :local:


奥术 (Arcane)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 奥术飞弹 (skillname), 38704
- 魔爆术 (skillname), 27082
- 奥术冲击 (skillname), 30451
- 奥术弹幕 (skillname), 44780

其他技能:

- 闪现术 (skillname), 1953
- 唤醒 (skillname), 12051
- 法术反制 (skillname), 2139
- 法术偷取 (skillname), 30449
- 隐形术 (skillname), 66
- 解除诅咒 (skillname), 475
- 缓落术 (skillname), 130


火焰 (Fire)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 火球术 (skillname), 38692
- 炎爆术 (skillname), 33938
- 灼烧 (skillname), 27074
- 火焰冲击 (skillname), 27079
- 烈焰风暴 (skillname), 27086
- 霜火箭 (skillname), xxxxx
- 龙息术 (skillname), 33043
- 冲击波 (skillname), 33933
- 活动炸弹 (skillname), 55359


冰霜 (Frost)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 寒冰箭 (skillname), 38697
- 冰枪术 (skillname), 30455
- 冰霜新星 (skillname), 27088
- 冰锥术 (skillname), 27087
- 暴风雪 (skillname), 27085
- 寒冰屏障 (skillname), 45438


自我Buff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 冰甲术 (skillname), 43008
- 法师护甲 (skillname), 43024
- 熔岩护甲 (skillname), 43046


团队Buff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 奥术智慧 (skillname), 42995
- 奥术光辉 (skillname), 43002
- 魔法增效 (skillname), 43017
- 魔法抑制 (skillname), 43015


护盾
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 法力护盾 (skillname), 43020
- 寒冰护体 (skillname), 43039
- 防护火焰结界 (skillname), 43010
- 防护冰霜结界 (skillname), 43012


补给
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 造魔法酪饼 (skillname), 42956
- 召唤餐桌 (skillname), 58659
- 制造法力宝石 (skillname), 42985


传送
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
传送技能:

联盟:

- 暴风城 (传送): 3561
- 暴风城 (传送门): 10059

- 铁炉堡 (传送): 3562
- 铁炉堡 (传送门): 11416

- 达纳苏斯 (传送): 3565
- 达纳苏斯 (传送门): 11419

- 埃索达 (传送): 32271
- 埃索达 (传送门): 32266

- 塞拉摩(传送): 49359
- 塞拉摩 (传送门): 49360

部落:

- 奥格瑞玛 (传送): 3567
- 奥格瑞玛 (传送门): 11417

- 雷霆崖 (传送): 3566
- 雷霆崖 (传送门): 11420

- 幽暗城 (传送): 3563
- 幽暗城 (传送门): 11418

- 银月城 (传送): 32272
- 银月城 (传送门): 32267

- 斯通纳德 (传送): 49358
- 斯通纳德 (传送门): 49361

中立:

- 沙塔斯城 (传送): 33690 (联盟版) / 35715 (部落版)
- 沙塔斯城 (传送门): 33691 (联盟版) / 35717 (部落版)
- 达拉然 (传送): 53140
- 达拉然 (传送门): 53142


变形术
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 变羊: 12826
- 变乌龟: 28271
- 变蛇: 61025
- 变猫: 61305
- 变兔子: 61721
- 变火鸡: 61780


.. _术士技能ID:

术士 (Warlock)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/09-Warlock.png
    :height: 128px
    :width: 128px

直接学习所有需要做任务才能获得的技能::

    /target player
    .learn 697 召唤 虚空行者
    .learn 712 召唤 魅魔
    .learn 691 召唤 地狱猎犬
    .learn 1122 召唤 地狱火


痛苦 (Affliction)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 腐蚀术 (skillname), 27216
- 痛苦无常 (skillname), 30405
- 鬼影缠身 (skillname), 59161
- 腐蚀之种 (skillname), 27243

诅咒:

- 痛苦诅咒 (skillname), 27218
- 虚弱诅咒 (skillname), 27224
- 鲁莽诅咒 (skillname), 27226
- 元素诅咒 (skillname), 27228
- 虚弱诅咒 (skillname), 30909
- 厄运诅咒 (skillname), 30910
- 语言诅咒 (skillname), 11719

- 生命分流 (skillname), 27222

- 吸取灵魂 (skillname), 27217
- 吸取生命 (skillname), 27220
- 吸取法力 (skillname), 30908
- 生命虹吸 (skillname), 30911
- 死亡缠绕 (skillname), 47860

- 暗影防护结界 (skillname), 28610

- 恐惧 (skillname), 6215
- 恐惧嚎叫 (skillname), 17928


恶魔 (Demonology)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
召唤恶魔:

- 召唤小鬼 (skillname), 688
- 召唤虚空行者 (skillname), 697
- 召唤魅魔 (skillname), 712
- 召唤地狱猎犬 (skillname), 691
- 召唤地狱火 (skillname), 1122
- 召唤末日仪式 (skillname), 18540
- 奴役恶魔 (skillname), 11726

- 生命通道 (skillname), 27259
- 黑暗契约 (skillname), 27265

各种石头:

- 制造治疗石 (skillname), 27230
- 制造火焰石 (skillname), 27250
- 制造法术石 (skillname), 28172
- 制造灵魂石 (skillname), 27238

术士护甲:

- 魔甲术 (skillname), 27260
- 邪甲术 (skillname), 28189

- 召唤仪式 (skillname), 698
- 灵魂仪式 (skillname), 29893

- 灵魂碎裂 (skillname), 29858
- 基尔罗格之眼 (skillname), 126
- 侦测隐形 (skillname), 132
- 感知恶魔 (skillname), 5500
- 魔息术 (skillname), 5697

- 放逐术 (skillname), 18647


毁灭 (Destruction)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
单体:

- 暗影箭 (skillname), 27209
- 献祭 (skillname), 27215
- 灼热之痛 (skillname), 30459
- 灵魂之火 (skillname), 30545
- 暗影灼烧 (skillname), 30546
- 燃烧 (skillname), 30912
- 烧尽 (skillname), 32231
- 混乱之箭 (skillname), 59170

AOE:

- 火焰之雨 (skillname), 27212
- 地狱烈焰 (skillname), 27213
- 暗影之怒 (skillname), 30414
- 暗影烈焰 (skillname), 61290


.. _牧师技能ID:

牧师 (Priest)
-------------------------------------------------------------------------------
.. image:: /_static/image/class-icon/10-Priest.png
    :height: 128px
    :width: 128px


Buff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 真言术：韧 (skillname), 25389
- 坚韧祷言 (skillname), 25392

- 神圣之灵 (skillname), 25312
- 精神祷言 (skillname), 32999

- 防护暗影 (skillname), 25433
- 暗影防护祷言 (skillname), 39374


戒律 (Discipline)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 真言术：盾 (skillname), 25218

- 心灵之火 (skillname), 25431
- 防护恐惧结界 (skillname), 6346
- 苦修 (skillname), xxxxx

- 驱散 (skillname), xxxxx
- 群体驱散 (skillname), 32375


神圣 (Holy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
神圣伤害:

- 惩击 (skillname), 25364
- 神圣之火 (skillname), 25384

治疗术:

- 恢复 (skillname), 25222
- 快速治疗 (skillname), 25235
- 次级治疗术 (skillname), 2053
- 治疗术 (skillname), 6064
- 强效治疗术 (skillname), 25213
- 神圣新星 (skillname), 25331
- 治疗祷言 (skillname), 25308
- 联结治疗 (skillname), 32546
- 愈合祷言 (skillname), 33076
- 治疗之环 (skillname), 34866
- 光明之泉 (skillname), 28275
- 绝望祷言 (skillname), 25437

- 驱除疾病 (skillname), 552
- 祛病术 (skillname), 528

- 复活术 (skillname), 25435
- 束缚亡灵 (skillname), 10955
- 漂浮术 (skillname), 1706


暗影 (Shadow)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 暗言术：痛 (skillname), 25368
- 暗言术：灭 (skillname), 32996
- 精神鞭笞 (skillname), 25387
- 心灵震爆 (skillname), 25375
- 噬灵瘟疫 (skillname), 25467
- 吸血鬼之触 (skillname), 34917


- 心灵尖啸 (skillname), 10888
- 渐隐术 (skillname), 586

- 暗影恶魔 (skillname), 34433
- 精神控制 (skillname), 605
- 心灵视界 (skillname), 10909
- 安抚心灵 (skillname), 453
- 法力燃烧 (skillname), 25380
