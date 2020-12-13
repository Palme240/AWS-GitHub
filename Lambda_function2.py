import boto3
import json

def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    response = table.put_item(Item = event)
    print(json.dumps(response))
    print("Row-" + str(index) + " written to DynamoDB successfully")
