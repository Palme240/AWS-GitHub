import boto3
import json
def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    body = json.loads(event['body'])
    table.put_item(Item = body)
    return {"statusCode": 200, "body": "Customer Added Successfully"}
