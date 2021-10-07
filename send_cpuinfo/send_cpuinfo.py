#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import boto3
import psutil
import datetime
from pytz import timezone

TOPIC_ARN = 'arn:aws:sns:ap-northeast-1:xxxx:xxx-topic'
INSTANCE_ID = 'i-xxxx'
REGION = 'ap-northeast-1'
now = str(datetime.datetime.now(timezone('Asia/Tokyo')))
subject = 'CPU利用率_' + now
sns_client = boto3.client('sns',region_name=REGION)
cloudwatch_client = boto3.client('cloudwatch', region_name=REGION)

# CPU使用率
cpu_info = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
          {
            'Name': 'InstanceId',
            'Value': INSTANCE_ID
          },
        ],
        StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=600),
        EndTime=datetime.datetime.utcnow(),
        Period=60,
        Statistics=['Maximum','Average']
)

msg = str(cpu_info['Datapoints'][0]['Average'])
response = sns_client.publish(
        TopicArn = TOPIC_ARN,
        Message = msg,
        Subject = subject
        )
if response['ResponseMetadata']['HTTPStatusCode'] != 200:
    print(error)
else:
    print(now,msg,"%")

