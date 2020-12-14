import boto3
import json
def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    print (event)
    body = json.loads(event['body'])
    response = table.put_item(Item = body)
    
    print(json.dumps(response))
    print("Row-" + str(index) + " written to DynamoDB successfully")
