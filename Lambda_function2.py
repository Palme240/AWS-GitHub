import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CUSTOMERS')
def lambda_handler2(event, context):
    table.put_item(Item=event)
    return str(event)
