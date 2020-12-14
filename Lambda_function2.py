import boto3
import json

def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
    table = dynamodb.Table('CUSTOMERS')

    response = table.put_item(Item = event)
    it = json.loads(event['records'][0]['data'])
    response = table.put_item(Item = it)
    print(json.dumps(response))
    print("Row-" + str(index) + " written to DynamoDB successfully")
    
    return {
            'statusCode': 200,
            "headers": {"Content-Type": "application/json"},
            'body': json.loads(json_data)
            }

    

