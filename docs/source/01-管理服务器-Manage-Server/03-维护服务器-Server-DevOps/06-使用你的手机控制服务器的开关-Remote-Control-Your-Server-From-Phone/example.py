# -*- coding: utf-8 -*-

import boto3

ssm_client = boto3.client("ssm")


def send_command(
    instance_id: str,
    cmd: str,
):
    ssm_client.send_command(
        InstanceIds=[
            instance_id,
        ],
        DocumentName="AWS-RunShellScript",
        DocumentVersion="1",
        Parameters={
            "commands": [
                cmd,
            ]
        }
    )


send_command(
    instance_id="i-1a2b3c4d",
    cmd="echo 1a2b3c4d > /home/ubuntu/chore",
)
