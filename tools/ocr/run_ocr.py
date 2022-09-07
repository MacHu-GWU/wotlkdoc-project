# -*- coding: utf-8 -*-

import boto3
import json
from pathlib_mate import Path
from s3pathlib import S3Path, context

boto_ses = boto3.session.Session(profile_name="sanhe_dev_us_east_1")
context.attach_boto_session(boto_ses)
tt_client = boto_ses.client("textract")
s3path_prefix = S3Path.from_s3_uri("s3://aws-data-lab-sanhe-for-everything/data/textract/")

def do_ocr(path: str):
    p = Path(path)
    p_new = p.change(new_ext=".json")
    s3path = s3path_prefix / p.basename
    s3path.write_bytes(p.read_bytes())
    res = tt_client.detect_document_text(
        Document=dict(
            S3Object=dict(
                Bucket=s3path.bucket,
                Name=s3path.key,
            )
        )
    )
    p_new.write_text(json.dumps(res))



do_ocr(
    "/Users/sanhehu/Documents/GitHub/wotlkdoc-project/docs/tmp/03-游戏指导 (Game Guide)/03-冲声望攻略 (Reputation)/02-TBC/2.4太阳井之怒新声望破碎残阳崇拜指南.png"
)