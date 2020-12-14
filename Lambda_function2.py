import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    table.put_item(Item = event, Key)
    
    return {"Code": 200, "body": json.dumps(result["Items"])}

    

