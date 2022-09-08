AWS RDS MySQL (其他数据库同理) 有两种备份方式. 一种是基于磁盘全盘备份的 Snapshot, 它记录了某个时刻数据库的全部磁盘的状态. 一种是基于 binlog 的全部历史日志, 可以从 0 恢复数据库.

基于 Snapshot 的方法

优势:

1. AWS 负责自动每天备份和管理
2. 一键从 Snapshot 恢复数据
3. 无需登录, 备份过程容易被自动化

缺点:

1. 收费
2. 如果你的 AWS Account 不用了, 导出比较复杂, 需要分享 KMS key

基于 MySQL Dump 的方法

优势:

1. 备份的内容是数据库中的数据文件, 你有更多的控制

缺点:

1. 需要手动执行, 不容易被自动化


基于 Snapshot 的备份和恢复
------------------------------------------------------------------------------
**备份**



基于 MySQL Dump 的备份和恢复
------------------------------------------------------------------------------

参考资料:

- Backup and Recovery Using MySQL Dump: https://dev.mysql.com/doc/mysql-backup-excerpt/5.7/en/using-mysqldump.html