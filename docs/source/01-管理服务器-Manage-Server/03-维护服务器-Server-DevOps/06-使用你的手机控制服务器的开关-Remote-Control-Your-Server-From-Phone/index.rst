.. _remote-control-your-server-from-phone:

使用你的手机控制服务器的开关 Remote Control Your Server From Phone
==============================================================================
无论是单机玩家还是服务器管理员, 如果能从你的手机上对服务器进行一些简单的控制, 例如查询状态, 启动, 关闭, 重启, 那简直是太棒了.


1. 如何用你的手机远程控制服务器.
2. 如何优雅的在服务器上远程执行命令.


如何用手机远程控制服务器
------------------------------------------------------------------------------
首先我们的手机不是一个电脑设备, 在手机上配置软件, 并且像在终端中敲命令那样使用手机是完全不现实的. 一个比较现实的情况就是银行的手机短信银行的方式. 你预先定义好一些操作码, 然后发送操作码到特定的电话号码, 然后会收到自动回复以用来展示一些信息. 这比你开发一个 Web App, 然后用手机登录 Web App 操作要省事多了.

AWS Pinpoint 服务器就支持这个功能, 你可以申请一个号码作为你的虚拟客服, 然后用你的手机给这个号码发短信. 你的短信会被发送到一个 AWS SNS Topic 上, 然后你可以用 AWS Lambda Subscribe 这个 Topic, 于是便可以根据你发送的短信让 Lambda 来做任何事情了. 因为 Lambda 里面可以运行各种编程语言和命令, 这里的想象力是无穷的.

参考文档:

- https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-two-way.html


如何优雅的在服务器上远程执行命令
------------------------------------------------------------------------------
通常我们都是用 SSH 登录服务器, 然后再终端里敲命令. 这样还是有登陆, 以及手动输命令的过程, 无法被自动化, 不够优雅.

AWS 有一个历史悠久的服务 SSM (System Manager). 你在启动 EC2 的时候, 如果给其配备的 IAM Role 里包含这个由 AWS 管理的 IAM Policy ``arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM``, 那么 EC2 会自动安装 SSM Agent. 这个 Agent 就能允许你在 AWS Console 或是用 SSM API 在 EC2 上远程执行命令.

请看一段 Python 代码的例子:

.. literalinclude:: ./example.py
   :language: python


- https://aws.amazon.com/getting-started/hands-on/remotely-run-commands-ec2-instance-systems-manager/
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.send_command