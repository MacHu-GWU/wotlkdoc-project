# -*- coding: utf-8 -*-

from s3pathlib import context
from boto_session_manager import BotoSesManager, AwsServiceEnum

bsm = BotoSesManager(profile_name="aws_data_lab_sanhe_us_east_1")

ec2_client = bsm.get_client(AwsServiceEnum.EC2)

context.attach_boto_session(bsm.boto_ses)
