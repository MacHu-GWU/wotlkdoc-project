/*
本段 SQL 代码的作用是:

1. 创建一个 database user 供服务端程序使用. 这个用户的名字, 密码等信息需要在 authserver.conf 和 worldserver.conf 中使用.
2. 给与这个 user 较大的权限 (几乎所有) 使得服务端程序能对数据库进行各种操作.
3. 创建必须的三个 database.

本段代码来自于 AzerothCore 官方 GitHub 仓库: https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql
*/
-- 先删除已经存在的叫做 acore 的 user, 后面的这个 localhost 表示这个 user 将要从哪里访问
-- 对于服务端程序和数据库在同一个机子上的情况, 当然要用 localhost 了
DROP USER IF EXISTS 'acore'@'localhost';
-- 创建一个叫 acore 的 user, 并指定它将会从 localhost 来访问, 而 IDENTIFIED BY 'acore' 则是说设定该服务器的密码为 acore
-- MySQL CREATE USER 命令的官方文档: https://dev.mysql.com/doc/refman/8.0/en/create-user.html
CREATE USER 'acore'@'localhost' IDENTIFIED BY 'acore' WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0;
-- 给这个用户所有的数据库权限, 后面的 WITH GRANT OPTION 是指它不仅自己有这些权限, 还能将这些权限 GRANT 给别人
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'localhost' WITH GRANT OPTION;
-- 创建需要的三个数据库, 没什么好说的
CREATE DATABASE `acore_world` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_general_ci;
CREATE DATABASE `acore_characters` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_general_ci;
CREATE DATABASE `acore_auth` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_general_ci;
-- 给之前创建的 user 对于三个数据库的最大权限
GRANT ALL PRIVILEGES ON `acore_world` . * TO 'acore'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON `acore_characters` . * TO 'acore'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON `acore_auth` . * TO 'acore'@'localhost' WITH GRANT OPTION;
