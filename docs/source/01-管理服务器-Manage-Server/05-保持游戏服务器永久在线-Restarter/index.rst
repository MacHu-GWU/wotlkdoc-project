.. _linux-restarter:

保持游戏服务器永久在线 Restarter
==============================================================================
Keywords:

此文档介绍了当你用 Linux (最好是 Ubuntu) 来部署服务器时, 如何保持服务器 24 小时在线的方法.


挑战
------------------------------------------------------------------------------
1. 在本地单机上你的机器不可能 24 小时开机, 而且你有可能误操作关闭了游戏服务器命令行窗口.
2. 对于云端部署的情况你通常是用 SSH 连接到远程服务器上然后运行的 authserver / worldserver, 一旦你的 SSH 断开, 远端运行的服务也会断开. 就算你在本地将 SSH 窗口保持不断开, 但你本地机器总是有可能要关机的 (参考 1).
3. 游戏服务器 authserver / worldserver 进程有可能会挂掉, 你不可能每次挂掉就立刻 SSH 到服务器上重启.


GNU screen 工具
------------------------------------------------------------------------------
Screen 是一个命令行工具. 它提供了从多个终端窗口连接到同一个 shell 会话 (会话共享). 当网络中断, 或终端窗口意外关闭是, 中 screen 中运行的程序任然可以运行. 相比之下当系统自带的终端窗口意外关闭时, 在该终端窗口中运行的程序也会终止.

从逻辑上 Screen 相当于能把任何脚本, 命令转为后台运行, 并且允许你随时切换到这个后台运行的 session, 也就是你用起来跟你在 shell 里一样, 但实际上它还在后台. 不过 Screen 的实现原理跟 System Service 完全不一样, 它也不要求你的程序要符合 Service 的标准.

检查 Screen 的版本::

    screen --version

参考资料:

- GNU Screen 官网: https://www.gnu.org/software/screen/manual/screen.html


解决方案
------------------------------------------------------------------------------
先找到你构建的 Azeroth Server 的位置. ``cd`` 到 ``bin`` 目录.

然后在该目录下创建 4 个文件, 创建的时候请读一下里面的内容:

- ``auth.sh``: 用于每 20 秒一次如果检测到 authserver 挂了就自动重启
- ``world.sh``: 用于每 20 秒一次如果检测到 worldserver 挂了就自动重启
- ``restarter.sh``: 用 screen 命令对 ``auth.sh``, ``world.sh`` 进行封装, 将这两脚本以 screen session 的方式再后台运行.
- ``shutdown.sh``: 检测运行中的 screen session, 如果找到了就将其杀死

.. literalinclude:: ./auth.sh
   :language: bash

.. literalinclude:: ./world.sh
   :language: bash

.. literalinclude:: ./restarter.sh
   :language: bash

.. literalinclude:: ./shutdown.sh
   :language: bash

你可以用任何终端文本编辑器来创建这些脚本, 比如 `vim <https://www.vim.org/>`_ 或者 `nano <https://www.nano-editor.org/>`_.

默认情况下创建的脚本只能被创建者 (也就是你) 执行. 而我们需要让 ``restarter.sh`` 去调用 ``auth.sh`` 就不行了. 你需要打 ``chmod +x auth.sh``, ``chmod +x world.sh`` 将这两个脚本变成可执行的. 不然 ``restarter.sh`` 能够被成功运行, 但实际上没有成功 (后面的 auth / world 服务器没有被运行)


管理服务器
------------------------------------------------------------------------------
启动服务器, 但没有 world console 界面::

    ./restarter.sh

进入 world console session 界面, 如果你按 ctrl + d 退出, 那么这个 session 就被杀死了, 你可以按下 Ctrl + A, 然后按 D (按下 Ctrl + A 之后系统不会给你任何反馈, 你就按 D 就好了) 这样 session 还在::

    screen -r world

启动服务器并且进入 world console session 界面::

     ./restarter.sh; screen -r world

关闭服务器::

    ./shutdown.sh

参考资料:

- AzerothCore 项目的服务器自动重启脚本教程: https://www.azerothcore.org/wiki/linux-restarter
