单机版Solo团队副本
==============================================================================

在单机版中 Solo 团队副本一直是最有乐趣的部分. 可是由于单机版的局限性, 单机 Solo 团队副本的方式只有以下几种:

1. 修改人物的属性数值, 超高的 血, 防御, 攻击力, 治疗能力, 数值碾压. 乐趣较低.
2. 使用过 NPC Bot 机器人, 帮你一起打副本, 机器人跟玩家的互动配合性较差.
3. 使用 Multibox 多开, 配合一些 Buff, 单人操控多个角色.


正式服副本团队人员配置信息
------------------------------------------------------------------------------

注: 经典旧世中的坦克算 0.4 DPS, TBC 之后的坦克算作 0.5 DPS

- 5: 1 Tank, 3 DPS, 1 Healer (3.5 DPS)
- 10: 2 Tank, 5 DPS, 3 Healer (7 DPS)
- 25: 2 Tank, 17 DPS, 6 Healer (18 DPS)
- 40: 5 Tank, 23 DPS, 12 Healer (25 DPS)

ICC 毕业装备的 **护甲减伤**, 例如刚 80 的蓝装坦克减伤在 50% 左右, ICC 毕业后在 50%.

- 坦克: -70% (早期 -50%)
- 板甲DPS: -50% (早期 -40%)
- 锁甲拿盾萨满: -50% (早期 -40%)
- 锁甲不拿盾: -35% (早期 -30%)
- 皮甲: - 25% (不变)
- 布甲: - 15% (不变)


怪物血量设置
------------------------------------------------------------------------------
由于采用给玩家添加 造成的所有伤害增加 X% Buff 的方法, 在叠加公式的影响下, 会带来严重的叠加效果. 比如 圣骑士的腐化圣印, 以及火法的点燃, 在增加100%伤害的情况下, 实际情况是变成4倍伤害. 使得很难平衡职业. 所以采用在服务器端设置修改怪物的血量, 才是比较好的解决方案.


正常::

    #--- HP Rate ---
    Rate.Creature.Normal.HP          = 1
    Rate.Creature.Elite.Elite.HP     = 1
    Rate.Creature.Elite.RARE.HP      = 1
    Rate.Creature.Elite.RAREELITE.HP = 1
    Rate.Creature.Elite.WORLDBOSS.HP = 1


5人小队副本, 3.5 DPS, 1 / 3.5 = 0.286::

    #--- HP Rate 5 Dungeon, 3.5 DPS, 1 / 3.5 = 0.286 ---
    Rate.Creature.Normal.HP          = 0.286
    Rate.Creature.Elite.Elite.HP     = 0.286
    Rate.Creature.Elite.RARE.HP      = 0.286
    Rate.Creature.Elite.RAREELITE.HP = 0.286
    Rate.Creature.Elite.WORLDBOSS.HP = 0.286


10人团队副本, 7 DPS, 1 / 7 = 0.143::

    #--- HP Rate 10 Raid, 7 DPS, 1 / 7 = 0.143 ---
    Rate.Creature.Normal.HP          = 0.143
    Rate.Creature.Elite.Elite.HP     = 0.143
    Rate.Creature.Elite.RARE.HP      = 0.143
    Rate.Creature.Elite.RAREELITE.HP = 0.143
    Rate.Creature.Elite.WORLDBOSS.HP = 0.143


25人团队副本, 18 DPS, 1 / 18 = 0.055::

    #--- HP Rate 25 Raid, 18 DPS, 1 / 18 = 0.056 ---
    Rate.Creature.Normal.HP          = 1
    Rate.Creature.Elite.Elite.HP     = 1
    Rate.Creature.Elite.RARE.HP      = 1
    Rate.Creature.Elite.RAREELITE.HP = 1
    Rate.Creature.Elite.WORLDBOSS.HP = 1


40人团队副本, 23 DPS, 1 / 25 = 0.04::

    #--- HP Rate 40 Raid, 25 DPS, 1 / 25 = 0.04 ---
    Rate.Creature.Normal.HP          = 0.04
    Rate.Creature.Elite.Elite.HP     = 0.04
    Rate.Creature.Elite.RARE.HP      = 0.04
    Rate.Creature.Elite.RAREELITE.HP = 0.04
    Rate.Creature.Elite.WORLDBOSS.HP = 0.04



Solo 团队副本时的血量设置
------------------------------------------------------------------------------

按两下下面的宏, 将血量提升至4倍, 并每秒回复3%的生命 (Buff前生命的12%)

血限, +100%耐力::

    /target player
    .aura 71953
    .aura 19259
    .aura 19259
    .aura 19259
    .aura 19259
    .aura 19259
    .aura 19259
    .aura 19259
    .aura 19259
    .aura 19259
    .aura 19259


::

.aura 71953 每3秒为团队成员回复3%的生命
.unaura 19259 降低所有伤害降低6%


减伤系数"

- **板甲DPS**, 40%, 最终减伤 (1 - 0.5 * (1 - 40%)) = 70%::

    /target player
    .unaura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383

- **锁甲拿盾萨满**, 40%, 最终减伤 (1 - 0.5 * (1 - 40%)) = 70%::

    /target player
    .unaura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383

- **锁甲不拿盾**, 54%, 最终减伤 (1 - 0.5 * (1 - 54%)) = 70%::

    /target player
    .unaura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383

- **皮甲**, 60%, 最终减伤 (1 - 0.75 * (1 - 60%)) = 70%::

    /target player
    .unaura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383

- **布甲**, 65%, 最终减伤 (1 - 0.85 * (1 - 65%)) = 70%::

    /target player
    .unaura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383
    .aura 31383

30

75

- 85

三开坦克输出治疗, Multibox玩法
------------------------------------------------------------------------------

开 3 个客户端, 一个坦克, 一个输出, 一个治疗. 使用 Multibox 软件同时控制三个人物.

- 10人副本: 0.2 (20%, 1/5) 血量, 算2坦克3治疗5DPS.
- 25人副本: 0.0625 (6.25%, 1/16) 血量, 算2坦克7治疗16DPS.

所有人Buff::

    .aura 29476 [星界护甲] 收到的伤害-90%, 永久持续, 可与其他Buff叠加
    .aura 73828 [乌瑞恩之力] +30%最大HP, 造成的伤害, 造成的治疗效果

坦克Buff::

    .aura xxx

输出Buff::

    .aura xxx

治疗Buff::

    .aura 71953 [烈光之环] 每3秒治疗周围盟友相当于其生命上限3%的生命值


