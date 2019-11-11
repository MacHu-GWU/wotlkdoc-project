.. _ClientFileSystem:

魔兽世界客户端文件详解 (WOW Client File System)
===============================================================================

.. image:: WOWClientGuide.png


动作条键位信息
-------------------------------------------------------------------------------
``account_name`` 是你登陆游戏时的账号

键位有两种设置, 通用设置和角色设置。

- 通用设置文件保存在 ``World of Warcraft/WTF/Account/<account_name>/bindings-cache.wtf``
- 角色设置文件保存在 ``World of Warcraft/WTF/Account/<account_name>/<server_name>/<character_name>/bindings-cache.wtf``


动作条摆放设置
------------------------------------------------------------------------------
每个动作条上摆了什么技能的记录保存在服务器的数据库中.


宏命令信息
-------------------------------------------------------------------------------
宏命令也有两种设置, 通用设置和角色设置。

- 通用设置文件保存在 ``World of Warcraft/WTF/Account/<account_name>/macros-cache.txt``
- 角色设置文件保存在 ``World of Warcraft/WTF/Account/<account_name>/<server_name>/<character_name>/bindings-cache.wtf``, ``macros-cache.txt``


插件设置
-------------------------------------------------------------------------------
魔兽世界的插件文件是以文件夹的形式保存在 ``World of Warcraft/Interface/AddOns`` 目录下的。插件产生的数据并不保存在这儿, 而是根据账号和角色名保存在 ``World of Warcraft/WTF`` 目录下。每次登陆游戏时, 系统会自动创建一系列以 ``Blizzard`` 开头的插件。


游戏内数据缓存
-------------------------------------------------------------------------------
鼠标移动到item, npc, object上所显示的面板, 是用到了 ``World of Warcraft/Cache/WDB/zhTW`` 目录下的缓存文件。``itemcache.wdb`` 文件最大, 最有备份价值。台服, 美服, 国服的cache文件不可以通用。


WTF 文件夹内的文件说明
------------------------------------------------------------------------------

- ``/WTF``
- ``/WTF/Config.wtf``: Resolution, Video, Audio Setting. Globally available to any account. (客户端设定, 图像质量, 圣印)
- ``/WTF/Account``
- ``/WTF/Account/<account_id>``: Per Account Setting (on different server, different character)
- ``/WTF/Account/<account_id>/bindings-cache.wtf``: Key binding. (快捷键设置)
- ``/WTF/Account/<account_id>/macros-cache.txt``: general macro config. will be used for all server, all character (通用宏命令设置)
- ``/WTF/Account/<account_id>/config-cache.txt``: game interface config, like auto-loot,  display percentage text (用户界面设置, 比如自动拾取, 显示百分比等)
- ``/WTF/Account/<account_id>/cache.md5``: all cache file md5, if you want to copy your account level config files to other place, copy this file with them.
- ``/WTF/Account/<account_id>/SavedVariables/``: addons global config setting, like default profile. (插件的通用设置, 比如domino的动作条设置, 如果你要将该账号下的设置应用到其他账号, 请拷贝整个文件夹)
- ``/WTF/Account/<account_id>/<server_id>/<character_name>/AddOns.txt``: choose to enable or disable which addons. (选择开启或关闭哪些插件)
- ``/WTF/Account/<account_id>/<server_id>/<character_name>/bindings-cache.wtf``: character only key binding config. (角色专用快捷键设置)
- ``/WTF/Account/<account_id>/<server_id>/<character_name>/chat-cache.txt``: chat window config and cache. (聊天窗口设置)
- /WTF``/Account/<account_id>/<server_id>/<character_name>/config-cache.wtf``: additional interface config, like talend previewer(额外的用户界面设置, 例如天赋浏览器)
- ``/WTF/Account/<account_id>/<server_id>/<character_name>/layout-local.txt``: character only interface window layout (用户界面布局, 各个窗口的位置)
- ``/WTF/Account/<account_id>/<server_id>/<character_name>/macros-cache.txt``: character only macro (角色专用宏命令)
- ``/WTF/Account/<account_id>/<server_id>/<character_name>/SavedVariables/``: character only addon config (角色专用的插件设置)
