import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CUSTOMERS')
def lambda_handler2(event, context):
    table.put_item(Item=event)
    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true'
        },
        "body": json.dumps(Item)
    }
    return response
