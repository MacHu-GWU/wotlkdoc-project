AzerothCore AWS Installation Guide
==============================================================================



本教程写于 2022-09-01. 我个人的所有服务器配置是用 Mac 做的, 因为 Mac 上有跟 Linux 一致的命令行. 比较方便. 而 Windows 仅仅是用来玩游戏.


1. AWS Console 准备工作
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
这一步主要是为 EC2 服务器创建所需的网络资源, 配置安全策略等.

AWS 准备工作概览:

1. 为你的服务器准备一个固定 IP, 不然这个 IP 在每次 EC2 重启后都会换, 导致你需要改服务器和客户端的配置. 参考文档:
    - How do I associate a static public IP address with my EC2 Windows or Linux instance?: https://aws.amazon.com/premiumsupport/knowledge-center/ec2-associate-static-public-ip/
2. 为你的服务器准备一个 Security Group, 这相当于防火墙, 能指定谁能从哪里走网络连接到我的服务器. 建议使用 Inbound Traffic = All traffic FROM your IP address.
3. 在 Public Subnet 上创建一个 Ubuntu 20 的服务器 (千万不要用 Ubuntu 22, 因为 Azeroth Core 不支持 OpenSSL 3.X+, 而 Ubuntu 22 以后都是默认 OpenSSL 3.X + 了), 建议用 t3.xlarge 也就是 4 个 vCPU, 16G 内存 ($0.1664 / Hour, $3.9936 / Day, $119.808 / Month, 100GB 硬盘, 参考文档:
    - Installation Guide, Linux Requirements: https://www.azerothcore.org/wiki/linux-requirements
4. 创建一个 EC2 Key Pair 并将其下载到本地, 这将是你用于远程登录 Linux 服务器的钥匙. 参考文档:
    - Amazon EC2 key pairs and Linux instances: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
5. 下载 DBeaver 开源万能数据库连接软件.


2. Linux Requirements 服务器准备工作
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
由于服务器核心的代码是用 C++ 写的, 而 C++ 代码需要在对应的平台 (Linux, Windows) 先编译成可执行机器码才能运行. 而编译是需要很多工具链的. 除此之外我们还需数据库软件来运行服务器数据库. 这一步的主要任务就是安装这些工具链.

总结来说我们需要以下依赖::

    MySQL ≥ 5.7.0
    Boost ≥ 1.74
    OpenSSL ≥ 1.0.x (OpenSSL 3.0 is not supported)
    CMake ≥ 3.16
    Clang ≥ 10

如果你要用 MariaDB (MySQL 的开源版), 命令如下, 请注意 Azeroth Core 只支持 10.6 and 10.5::

    sudo apt update && sudo apt full-upgrade -y && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev mariadb-server mariadb-client libmariadb-dev libmariadb-dev-compat

而如果你要用 MySQL 8.X 命令如下::

    sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libboost-all-dev

之后我们来安装一下开发者工具, 这些工具 Ubuntu 上一般预装的, 我们先检查一下它们的版本, 如果版本不对则再更新一下. 请运行下面的命令检查版本::

    # OpenSSL 3.x is NOT SUPPORTED. Please use 1.x or 2.x
    openssl version

    Your clang version MUST be 10 or higher
    clang --version

    # Your cmake version MUST be 3.16 or higher.
    cmake --version

    # Ensure that the gcc-8 headers are installed
    gcc --version

如果有任何一个库的版本不对可以用下面的命令来安装新版本::

    # clang
    sudo apt-get install clang-10.0

    # cmake
    python -m pip install cmake
    python -m pip install --upgrade cmake

    # gcc
    sudo apt-get update
    sudo apt-get install g++-8 gcc-8

为了一些自动化和测试, 我们建议安装 Python, 而且最好不要用系统的 Python 以免搞乱了系统 Python 上预装的依赖. 这一步不是必须的. 我们可以用 `pyenv <https://github.com/pyenv/pyenv>`_ 这个工具来安装.

参考文档:

- Installation Guide, Linux Requirements: https://www.azerothcore.org/wiki/linux-requirements


2. Core Installation 安装核心
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
这一步的主要任务是将核心的源代码编译成可执行程序.

**SSH Connect to Ubuntu Server**::

    # 3.227.85.43 是我的 EIP 公网 IP, 你不用尝试攻击了, AWS 有防火墙的.
    # ~/ec2-pem/aws-data-lab-sanhe/us-east-1/aws-data-lab-sanhe-dev.pem 是我用来存放秘钥的路径.
    ssh -i ~/ec2-pem/aws-data-lab-sanhe/us-east-1/aws-data-lab-sanhe-dev.pem ubuntu@3.227.85.43
    ssh -i ~/ec2-pem/aws-data-lab-sanhe/us-east-1/aws-data-lab-sanhe-dev.pem ubuntu@34.200.233.47

确保此时你在 ``${HOME}`` 路径下, 你打 ``pwd`` 命令返回的是 ``/home/ubuntu`` 就说明是对的.

**从 GitHub 获取 Azeroth Core 源代码**::

    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore

**编译源代码**::

    # 创建并移动到 build 目录
    cd azerothcore
    mkdir build
    cd build

    **注意! 请确保你现在已经在 azerothcore/build 目录下了**

    # 在运行下面 CMake 代码之前, 下面的 $HOME/azeroth-server 是编译好的服务器路径, 你可以改, 也可以不改
    # 如果你改了之后, 后面的自动化代码也要跟着改
    cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static -DMODULES=static

    # 查看你的服务器有多少个 CPU 核心, 这个数字要作为参数用在后面的命令中
    nproc --all

    # 构建服务器, 这一步完成之后 $HOME/azeroth-server 里会出现一个 ``bin`` 和 ``etc`` 文件夹
    make -j 6
    make install

参考资料:

- https://www.azerothcore.org/wiki/linux-core-installation

3. Server Setup 安装服务器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
从这一步起, 我们就会需要用到比较复杂的自动化命令. 而直接在 Linux 上编辑文件, 拷贝脚本都是非常不方便的. 所以我们创建了一个 GitHub 仓库. 这样能让我们在本地电脑上编辑脚本, 然后在服务器上同步脚本后运行.

服务器是需要知道一些客户端数据的, 例如地图数据, 是用来判定你和目标之间是否有视野, 有没有被墙壁阻拦, 空气墙在哪里等. 这些地图数据文件很大, 不适合放在服务器代码上. 这些数据文件原本是用特殊工具从游戏客户端上提取出来的 (游戏客户端也有这些文件, 方便于在本地做计算, 客户端连上服务器后会比较服务器和自己的 MD5 值, 如果不对说明客户端作弊了) Azeroth Core 有使用这些工具的教程. 不过 Azeroth Core 团队还定期提取这些文件, 并发布供玩家下载.

**下载并解压数据文件**

    # 回到用户主目录
    cd $HOME

    # 创建一个目录
    mkdir data
    cd data

    # 打开 https://github.com/wowgaming/client-data/releases/ 页面
    # 右键点击 data.zip 查看下载链接, 例如目前版本的是 https://github.com/wowgaming/client-data/releases/download/v15/data.zip
    # 用 wget 命令下载
    wget https://github.com/wowgaming/client-data/releases/download/v15/data.zip

    # 安装 unzip 解压工具
    sudo apt install unzip

    # 解压 data.zip 文件, 此时会在 $HOME/data 目录下创建 5 个文件夹
    unzip data.zip

**编辑服务器配置文件**

玩过单机版的都知道这两个文件 ``authserver.conf``, ``worldserver.conf``, 它们分别控制了登陆服务器和游戏世界服务器的配置. 而编译好的核心会在 ``ls ~/azeroth-server/etc/`` 目录下有两个 ``authserver.conf.dist``, ``worldserver.conf.dist`` 文件, 它们是默认的配置文件的备份. ``dist`` 是 ``distribution`` 发布的意思. 建议不要动这两个文件, 而是将其拷贝一份, 去掉 ``.dist`` 后缀, 然后修改这个拷贝的文件.

这里由于直接在服务器上用 vim 来编辑是很不方便的, 所以我用了一个 GitHub 仓库, 并且在服务器上 Clone 了这个仓库. 这样我就可以在我的 Mac 电脑上编辑, 然后同步过去了.

::

    #
    ls ~/azeroth-server/etc/

.. code-block:: bash

    # 克隆你自己的 GitHub 仓库
    git clone https://${GH_TOKEN}@github.com/MacHu-GWU/wotlk_private_server-project.git
    https://github.com/MacHu-GWU/wotlk_private_server-project.git

.. code-block:: bash

    # 将编辑好的配置文件应用到服务器 (需要重启后才能生效)
    cd ~/wotlk_private_server-project
    git pull
    make apply-config
`
还记得我们刚才下载了一个 ``data.zip`` 文件并解压到 ``$HOME/data`` 目录下了吗. 服务器默认只会在自己的目录下找, 这样肯定找不到. 所以我们要修改 ``worldserver.conf`` 文件, 搜索 ``DataDir``, 然后填入 ``/home/ubuntu/data`` (这是 ``$HOME/data`` 的绝对路径) 然后保存.

参考资料:

- Installation Guide - Server Setup: https://www.azerothcore.org/wiki/server-setup


Database Installation 安装数据库
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
这一步至关重要, 主要目的是运行数据库服务器, 将初始游戏数据写入数据库, 并学会如何连接数据库.

目前的状态是在 "Linux Requirements 服务器准备工作" 这一步我们已经安装了 MySQL 数据库, 但数据库并没有运行, 里面也没有任何数据. 首先我们要学会如何启动数据库, 并且用 root 账号连接数据库:

    # 启动 MySQL 数据库
    sudo service mysql start

    # 查看所有服务的状态
    sudo service --status-all

    # 关闭 MySQL 数据库
    sudo service mysql stop

    # 用 root 使用 MySQL client 从服务器上连接本地数据库 (不是从你的个人电脑连接)
    sudo mysql

目前数据库已经启动了, 但是里面没有任何数据. 我们先要创建空的数据库, 这样游戏核心才能往里面插入游戏数据. 我们先到 https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql, 这个是你需要运行的 SQL 命令, 能帮你创建空的数据库.

    # 连接数据库
    sudo mysql

    # 拷贝 create_mysql.sql 文件中的命令并运行.

至此空的数据库已经被创建了, 但里面没有任何数据. 当你启用游戏服务器的时候, 服务器会自动往数据库内写入并更新数据 (不会动你的游戏角色, 账号数据的). 服务器源代码里是包含了所有数据的 SQL 文件的, 你编译的时候就已经编译就能去了.

然后我们需要学会如何用 Dbeaver (或者其他 SQL 图形化界面) 从本地开发电脑连接到远程服务器上的 MySQL 数据库.

1. 下载 Dbeaver
2. 创建一个 MySQL 连接, 填入如下信息:
    - host = 127.0.0.1
    - port = 3306
    - database = acore_auth
    - username = acore
    - password = acore
3. 在 SSH 栏选择 SSH Tunnel 并填入以下信息. SSH Tunnel 技术的核心是你所有的流量都先发给远程 SSH 服务器, 然后从服务器连接 localhost
    - check "Use SSH Tunnel"
    - host 填写你的 EC2 的 EIP
    - port 22
    - username = ubuntu
    - authentication method = Public Key
    - private key = 你的 EC2 key ``.pem`` 文件的路径

参考资料:

- Installation Guide - Database Installation: https://www.azerothcore.org/wiki/database-installation:

Networking 配置网络
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
此时你的服务器是在 EC2 中的, 你需要进行一些配置才能让位于你本地电脑上的游戏客户端连接到服务器.

1. 首先用 Dbeaver 连接到数据库
2. 打开 acore_auth.realmlist 表
3. 把 address 一栏中的值改为你的服务器的 EIP 地址


Final Server Steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
每次你重启 EC2 后, 你要做以下三件事:

    # 启动数据库
    sudo service mysql start

    # 启动登录服务器
    ~/azeroth-server/bin/authserver

    # 启动游戏服务器
    ~/azeroth-server/bin/worldserver

    make apply-config


    Server Startup
    To start your server with the scripts, ensure you are in you server bin directory ~/azeroth-server/bin.
    We will start the restart scripts by typing the following command ./restarter.sh
    Side note: If you wish to start the server and see the worldserver console, use the following command ``./restarter.sh; screen -r world``
    Server Monitoring
    To access and view the Authserver or Worldserver consoles: -- Authserver: screen -r auth -- Worldserver: screen -r world
    When you want to exit the screen and return to your terminal, type Ctrl + A, followed by D.
    Server Shutdown
    To terminate the restarter and shutdown your server, ensure you are in you server bin directory ~/azeroth-server/bin.
    Type ./shutdown.sh and the scripts will turn off and your server will terminate.

cp auth.sh ~/azeroth-server/bin/auth.sh
cp world.sh ~/azeroth-server/bin/world.sh
cp restarter.sh ~/azeroth-server/bin/restarter.sh
cp shutdown.sh ~/azeroth-server/bin/shutdown.sh