import boto3
import json

def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    it = json.loads(event['records'][0]['data'])
    table.put_item(Item = it )
    
    return {"Code": 200, "message":"Customer Added Successfully"}

    

