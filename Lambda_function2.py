import boto3
import json
PARTTION_KEY = 'CUSTOMER_ID'
def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    table.put_item(Item= event)
    
    return {"Code": 200, "message":"Customer Added Successfully"}
