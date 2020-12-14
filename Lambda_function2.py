import boto3
def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    print (event)
    table.put_item(Item = event['body'])
    
    return {"Code": 200, "message":"Customer Added Successfully"}
