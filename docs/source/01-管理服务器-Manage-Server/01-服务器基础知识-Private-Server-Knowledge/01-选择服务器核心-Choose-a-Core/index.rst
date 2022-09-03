.. _choose-a-core:

选择服务器核心 Choose a Core
==============================================================================
魔兽世界私服本质上是完全不用暴雪的服务器代码 (因为从来没有泄露过), 自己用 C++ 实现的服务器功能, 包括地图管理, 副本管理, 怪物 AI 等等.

到 2022-09-01 为止, 目前有这么 3 个主流核心, 它们都有强大的社区和代码贡献者 (其他的魔改核心不算):

TrinityCore:

- https://www.trinitycore.org/
- https://github.com/TrinityCore/TrinityCore
- https://github.com/TrinityCore/TrinityCore/tree/3.3.5
- https://github.com/trickerer/Trinity-Bots
- https://github.com/trickerer/TrinityCore-3.3.5-with-NPCBots

MaNGOS:

- https://www.getmangos.eu/
- https://github.com/mangos/MaNGOS

AzerothCore:

- https://www.azerothcore.org/
- https://github.com/azerothcore/azerothcore-wotlk
- https://www.azerothcore.org/catalogue.html#/

TrinityCore 是一个超级老牌的开源项目. 目前市面上各种卖的 repack (自己编译打包后的服务端) 也是基于此. 它的目标是通用的, 不分版本的魔兽世界服务端, 一路支持所有的资料片到目前的 9.2 暗影国度. 这也导致了它无法对游戏内容和可玩性进行打磨, 只能专注于服务器技术. 而它的 3.3.5 是一个 branch, 也是它可玩性最好的版本.. 如果你是单机玩家, 由于项目本身不是专门为 3.3.5 版本服务的, 所以可玩性和修复上不如 AzerothCore. 如果你自己开服而且有技术团队, TrinityCore 的底层设计是最强大的, 你可以自己投入资源进行修复和魔改, 适合开服.

MaNGOS 比 TrinityCore 新, 但是也很老的项目. 它专注于 经典旧世, 燃烧的远征, 巫妖王之怒, 大灾变, 熊猫人之谜 5 个版本.

AzerothCore 是三个中最年轻的, 但是正因为年轻, 代码架构, 文档, 社区都很先进和完善. 它专注于提供可玩性和修复的最好的 3.3.5 版本. 如果你不想做过多的改动就自己开服玩, 不是面向公众的私服, AzerothCore 是最合适的.


我的选择
------------------------------------------------------------------------------
由于我只有一个人, 我选择 **AzerothCore** 作为游戏性最好, 最容易部署, 支持适当魔改的服务端核心.
