import boto3
import json

def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    table.put_item(Item=event)
    
    return {
            'statusCode': 200,
            'body': json.dumps('Succesfully inserted customer')
