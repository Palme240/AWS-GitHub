import boto3
import json
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CUSTOMERS')
   
def lambda_handler2(event, context):
   print(json.dumps(event))
   response = table.put_item(Item = event)
   print(json.dumps(response))
   print("Row-" + str(index) + " written to DynamoDB successfully")
    

