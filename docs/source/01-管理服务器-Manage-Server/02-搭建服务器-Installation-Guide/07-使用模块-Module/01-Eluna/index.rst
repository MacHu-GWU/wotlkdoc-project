Eluna
==============================================================================
Eluna 是一个允许你在服务端添加 Lua 脚本的模块. 本质上跟 WOW Addon 一样, 不过这是服务器端的 Lua 脚本. 功能非常强大.

- https://www.azerothcore.org/catalogue.html#/details/413964782
- https://github.com/azerothcore/mod-eluna
- https://www.azerothcore.org/pages/eluna/index.html

我们来看一段示例代码:

.. code-block:: lua

    local PLAYER_EVENT_ON_LOGIN = 3

    local function OnLogin(event, player)
        player:SendBroadcastMessage("Hello world")
    end

    RegisterPlayerEvent(PLAYER_EVENT_ON_LOGIN, OnLogin)

很明显, 这就是一个典型的事件驱动的程序.

``RegisterPlayerEvent`` 这是一个负责注册 PlayerEvent 的方法. 所有的 Register 都可以在这个文档 https://www.azerothcore.org/pages/eluna/Global/index.html 里找到. 这里面是所有的全局函数, 你搜索 Register 就可以看到所有可以用来注册的事件.

``PLAYER_EVENT_ON_LOGIN`` 定义了这具体是一个什么样的 PlayerEvent, 在这篇源码 https://github.com/ElunaLuaEngine/Eluna/blob/master/Hooks.h 中你可以找到对于不同类型的 Event, 每个具体的 Event Code 是什么.

而 ``OnLogin`` 则是一个函数, 用来处理 PlayerEvent 的数据. 这个函数具体有哪些参数同样可以在 https://github.com/ElunaLuaEngine/Eluna/blob/master/Hooks.h 中找到. 根据文档, 它有两个参数.


安装 mod_eluna 的坑
------------------------------------------------------------------------------

在 ``mod_LuaEngine.conf`` 配置文件中的 ``Eluna.ScriptPath`` 选项, 里面的路径最好用绝对路径而不要用相对路径.
