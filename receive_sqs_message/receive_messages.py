import boto3
import json

queue_url = "https://sqs.ap-northeast-1.amazonaws.com/xxxx/xxxx-queue"
region = "ap-northeast-1"

sqs_client = boto3.client("sqs", region_name=region)
while True:
    # 20秒のロングポーリング
    print("polling messages ...")
    response = sqs_client.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1, VisibilityTimeout=60, WaitTimeSeconds=20)
    isMessageExists = response.get("Messages")
    if isMessageExists:
        for res in response["Messages"]:
            if "Body" in res:
                elements = json.loads(res["Body"])
                print(elements["Subject"],"\n",elements["Message"],"%")
            # メッセージ削除        
            sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=res["ReceiptHandle"])
