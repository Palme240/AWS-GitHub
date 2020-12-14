import boto3
import os
import json 

dynamodb = boto3.resource('dynamodb')
   
def lambda_handler2(event, context): 
    table = dynamodb.Table('CUSTOMERS')
    data = json.loads(event['body'])
    table.put_item(
        Key={
            'id': data['id']
        }
    )              
    
    return {"Code": 200, "message":"Customer Added Successfully"}

