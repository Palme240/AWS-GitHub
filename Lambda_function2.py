import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CUSTOMERS')
def lambda_handler2(event, context):
    it = json.loads(event['records'][0]['data'])
    response = table.put_item(Item = it)
    return response
