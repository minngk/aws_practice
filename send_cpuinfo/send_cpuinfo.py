#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import boto3
import psutil
import datetime
from pytz import timezone

TOPIC_ARN = 'arn:aws:sns:ap-northeast-1:xxxxx:xxx-topic'

now = str(datetime.datetime.now(timezone('Asia/Tokyo')))
subject = 'CPU利用率_' + now
client = boto3.client('sns',region_name='ap-northeast-1')

# メモリ使用率
mem = psutil.virtual_memory()
msg = str(mem.percent)

response = client.publish(
        TopicArn = TOPIC_ARN,
        Message = msg,
        Subject = subject
        )
if response['ResponseMetadata']['HTTPStatusCode'] != 200:
    print("error http status code", response['ResponseMetadata']['HTTPStatusCode'])
else:
    print(now,msg,"%")