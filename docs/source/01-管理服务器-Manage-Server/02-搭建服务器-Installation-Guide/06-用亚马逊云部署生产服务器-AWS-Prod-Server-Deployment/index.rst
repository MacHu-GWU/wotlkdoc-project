.. _aws-prod-server-deployment:

用亚马逊云部署生产服务器 AWS Prod Server Deployment
==============================================================================
deploy azerothcore (AC) wotlk wow private server to AWS.


1. 架构选择
------------------------------------------------------------------------------
- 游戏服务器: 部署在位于 VPC Public Subnet 上的 EC2 中.
- 数据库: 使用 RDS MySQL. 注意, 请不要使用 Aurora MySQL compatible version. 因为 Aurora 的 Storage engine 是完全重新设计的, 和 MySQL 的完全不同. AC 的一些 SQL 要求使用旧款的 ``MyISAM`` 存储引擎, 这是 Aurora 所不支持的.


2. 为游戏服务器选择 EC2 Type
------------------------------------------------------------------------------
根据 AC Wiki 上 https://www.azerothcore.org/wiki/memory-usage 的说法, 当游戏玩家探索到一片地图后, 这个区域的地图就会被加载进内存, 而玩家多的时候几乎所有的地图都会被加载进内存, 这些地图至少占用 11G 左右. 而且操作系统本身大约会占用 1G 左右的内存. 而且大约每 100 个玩家需要占用 1G 内存. 你需要留给服务器大约 1 - 2G 内存左右供临时使用. 根据这篇 AC 上的讨论 https://github.com/azerothcore/azerothcore-wotlk/discussions/3891, 维护者 FrancescoBorzi 说了, CPU 一般不是瓶颈, 而 RAM 才是. < 200 个玩家的话, 16GB 内存是足够了的. 这和我们之前计算的 200 玩家 = 11G  + 2G + 1G = 占用 14G 内存一致.

我们再来看一个例子. 在官服, 一个服务器最大玩家容量在 3000 - 5000 左右, 按照 5000 玩家计算, 我们需要 5000 / 100 ~= 50G 内存, 加上 11G 地图和操作系统的 1G 大约是 62G 内存. 显然我们用 64G 内存的服务器会有随时崩溃的危险, 由于内存在 64 以上一般是 32G 一档, **所以对于 5000 玩家的服务器我们需要用 96G 内存的虚拟机比较合适**

**如何选择 AWS EC2 Type**

根据使用场景, 内存要够用, 在内存中对数据进行计算为主, 所以是内存够用, CPU 性能优先. 所以 T3 作为 General Purpose 的场景适合对性能要求不高, 小于 200 人的场景, 也比较便宜. 而对于更多的玩家, 我们就应该上 C6g Compute Optimized 服务器了, 因为 AWS 说明了它是适合游戏服务器的 EC2 类型.

**不同玩家数量下所需的 EC2 以及成本**

对于人数少的服务器我们通常使用按需付费模型, 随时停止缴费. 对于 1000 人以上的服务器通常就是以盈利为目的的了, 一般会用年度合约的方式节约成本.

- 纯单机玩家: 需要 4G 内存, 跑地图太多内存不够的化重启世界服务器即可, 选用 ``t3.medium`` 服务器, $1 一天, $30 一个月, $360 一年.
- 和朋友一起玩, 25 人以下: 需要 8G 内存, 一起玩一般不会满世界跑, 都是来做任务打副本的, 实在不行重启世界服务器即可, 选用 ``t3.large`` 服务器, $2 一天, $60 一个月, $720 一年.
- 开小型服务器, 200 人以下: 需要 16G 内存, 满负载时大约会占用 11 + 2 = 13G 左右内存, 选用 ``c6g.12xlarge`` 服务器, $6.528 一天, $196 一个月, $2,383 一年. 或者选用 ``t3.xlarge`` 服务器, $4 一天, $120 一个月, $1,457 一年.
- 开中型服务器, 1000 人以下: 需要 32G 内存, 满负载时大约会占用 11 + 8 = 20G 左右内存, 选用 ``c6g.4xlarge`` 服务器, $13.056 一天, $392 一个月, $4,765 一年
- 开大型服务器, 3000 人以下: 需要 64G 内存, 满负载时大约会占用 11 + 30 = 41G 左右内存, 选用 ``c6g.8xlarge`` 服务器, 一年 $5,604
- 开超大型服务器, 5000 人以下: 需要 96G 内存, 满负载时大约会占用 11 + 50 = 61G 左右内存, 选用 ``c6g.12xlarge`` 服务器, 一年 $8,406
- 开超大型服务器, 12000 人以下: 需要 192G 内存, 满负载时大约会占用 11 + 120 = 131G 左右内存, 选用 ``c6a.24xlarge`` 服务器, 一年 $19,860

参考资料:

- Instant Type: https://aws.amazon.com/ec2/instance-types/
- Pay as you go: https://aws.amazon.com/ec2/pricing/on-demand/
- Term contract: https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/


3. 为游戏数据库选择 Instance Type
------------------------------------------------------------------------------
选择合适的数据库大小要考虑两个维度:

1. 随着玩家数量的增加, 装备, 物品, 天赋等数量就会随之线性增加. 数据库引擎会将索引或是一些数据存在内存中, 以提高读写效率.
2. 同时在线的玩家数量增加, 需要将数据落盘的频率也就越高, 也就是俗称的 TPS 越多.

游戏本身的初始数据量大约在 200 MB 左右. 而每 1 个玩家的新增数据一般也就顶多 1 MB.

**不同玩家数量下所需的 Instance Type 以及成本**

- 纯单机玩家: 需要 1G 内存, 用 ``db.t4g.micro``, $0.384 一天, $11.52 一个月, $140 一年
- 200 人以下: 需要 2G 内存, 用 ``db.t4g.small``, $0.768 一天, $23 一个月, $280 一年
- 1000 人以下: 需要 4G 内存, 用 ``db.t4g.medium``, $1.536 一天, $46 一个月, $560 一年

参考资料:

- Instance Type: https://aws.amazon.com/rds/instance-types/
- Pricing: https://aws.amazon.com/rds/mysql/pricing/


4. 安装核心
------------------------------------------------------------------------------
这一步的主要任务是将核心的源代码编译成可执行程序.

**首先我们要 SSH 登录到 Ubuntu 服务器上**

.. code-block:: bash

    # 111.111.111.111 是你的 IP
    # /path/to/your/key/file.pem 是我用来存放秘钥的路径.
    ssh -i /path/to/your/key/file.pem ubuntu@111.111.111.111

第一次连接的时候会问你是否要将这个服务器添加为可信服务器, 打 Y 即可. 进去以后确认此时你在 ``${HOME}`` 路径下, 你打 ``pwd`` 命令返回的是 ``/home/ubuntu`` 就说明是对的.

**然后要从 GitHub 获取 Azeroth Core 源代码**

.. code-block:: bash

    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore

**从源码编译游戏服务器**

.. code-block:: bash

    # 移动到 azerothcore 仓库内
    cd azerothcore
    # 创建并移动到 build 目录
    mkdir build
    cd build
    # 注意! 请确保你现在已经在 azerothcore/build 目录下了, 打 pwd 命令返回的应该是 /home/ubuntu/azerothcore/build
    # 在运行下面 CMake 代码之前, 下面的 $HOME/azeroth-server 是编译好的服务器路径, 你可以改, 也可以不改
    # 如果你改了之后, 后面的自动化代码也要跟着改
    cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static -DMODULES=static

    # 查看你的服务器有多少个 CPU 核心, 这个数字要作为参数用在后面的命令中
    nproc --all

    # 构建服务器, 这一步完成之后 $HOME/azeroth-server 里会出现一个 ``bin`` 和 ``etc`` 文件夹
    make -j 4
    make install

**下载并解压地图数据文件**

服务器是需要知道一些客户端数据的, 例如地图数据, 是用来判定你和目标之间是否有视野, 有没有被墙壁阻拦, 空气墙在哪里等. 这些地图数据文件很大, 不适合放在服务器代码上. 这些数据文件原本是用特殊工具从游戏客户端上提取出来的 (游戏客户端也有这些文件, 方便于在本地做计算, 客户端连上服务器后会比较服务器和自己的 MD5 值, 如果不对说明客户端作弊了) Azeroth Core 有使用这些工具的教程. 不过 Azeroth Core 团队还定期提取这些文件, 并发布供玩家下载.

.. code-block:: bash

    # 回到用户主目录
    cd $HOME

    # 创建一个目录
    mkdir azeroth-server-data
    cd azeroth-server-data

    # 打开 https://github.com/wowgaming/client-data/releases/ 页面
    # 右键点击 data.zip 查看下载链接, 例如目前版本的是 https://github.com/wowgaming/client-data/releases/download/v15/data.zip
    # 用 wget 命令下载
    wget https://github.com/wowgaming/client-data/releases/download/v15/data.zip

    # 安装 unzip 解压工具
    sudo apt install unzip

    # 解压 data.zip 文件, 此时会在 $HOME/azeroth-server-data 目录下创建 5 个文件夹
    unzip data.zip

参考资料:

- https://www.azerothcore.org/wiki/linux-core-installation


5. 配置数据库
------------------------------------------------------------------------------
.. code-block:: bash

    mysql --host="prod-server.cluster-c7pwcs7oc5l0.us-east-1.rds.amazonaws.com" --user="admin" --password="gw8CH&wjRW%Q"

    SELECT user, host FROM mysql.user;
