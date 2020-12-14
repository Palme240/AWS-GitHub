import boto3
import json
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CUSTOMERS')
   
def lambda_handler2(event, context):
   response = table.put_item(Item = event)
   if not event.get('body'):
        return respond({"message": "PUT request requires parameters in the body"})

    try:
        body = json.loads(event['body'])
    except:
        return respond({
            "message": "PUT request requires JSON parameters in the body",
            "body": event['body']
        })
   print("Row-" + str(index) + " written to DynamoDB successfully")
    

