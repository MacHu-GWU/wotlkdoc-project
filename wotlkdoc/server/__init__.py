# -*- coding: utf-8 -*-

from ..boto_ses import ec2_client


def create_image():
    """
    从 EC2 Instance 创建 AMI. 不推荐自己运行这个命令, 建议在 EC2 Console 里选择 Instance
    然后点击 Create Image. 该操作耗时在 15-30 分钟. 取决于你的 EBS 快照的大小.

    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_image
    """
    # response = ec2_client.create_image(
    #     BlockDeviceMappings=[
    #         {
    #             'DeviceName': 'string',
    #             'VirtualName': 'string',
    #             'Ebs': {
    #                 'DeleteOnTermination': True | False,
    #                 'Iops': 123,
    #                 'SnapshotId': 'string',
    #                 'VolumeSize': 123,
    #                 'VolumeType': 'standard' | 'io1' | 'io2' | 'gp2' | 'sc1' | 'st1' | 'gp3',
    #                 'KmsKeyId': 'string',
    #                 'Throughput': 123,
    #                 'OutpostArn': 'string',
    #                 'Encrypted': True | False
    #             },
    #             'NoDevice': 'string'
    #         },
    #     ],
    #     Description='string',
    #     DryRun=True | False,
    #     InstanceId='string',
    #     Name='string',
    #     NoReboot=True | False,
    #     TagSpecifications=[
    #         {
    #             'Tags': [
    #                 {
    #                     'Key': 'string',
    #                     'Value': 'string'
    #                 },
    #             ]
    #         },
    #     ]
    # )


def create_store_image_task(
    image_id: str,
    bucket: str,
    tags: dict,
    dry_run: bool = True,
):
    """
    将创建好的 AMI 备份到 AWS S3, 使其更持久. 如果你要将 AMI 迁徙到其他 AWS 账号, 或者
    想进行长期的备份, 你可以先将其备份到 S3, 然后拷贝到其他 AWS 账号, 再从 S3 恢复为 AMI.
    然后你就可以用 AMI 创建 EC2 了.

    Reference

    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_store_image_task
    """
    return ec2_client.create_store_image_task(
        ImageId=image_id,
        Bucket=bucket,
        S3ObjectTags=[
            {
                "Key": key,
                "Value": value,
            }
            for key, value in tags.items()
        ],
        DryRun=dry_run,
    )


def create_restore_image_task(
    bucket: str,
    key: str,
    ami_name: str,
    ami_tags: dict,
    dry_run: bool = True,
):
    """
    从 S3 恢复 AMI 镜像.
    
    Reference:

    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_restore_image_task
    """
    return ec2_client.create_restore_image_task(
        Bucket=bucket,
        ObjectKey=key,
        Name=ami_name,
        TagSpecifications=[
            {
                "Tags": [
                    {
                        "Key": key_,
                        "Value": value,
                    }
                    for key_, value in ami_tags.items()
                ]
            },
        ],
        DryRun=dry_run,
    )
