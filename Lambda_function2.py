import boto3
def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    it = json.loads(event['records'][0]['data'])
    response = table.put_item(Item = it)
    print(json.dumps(response))
    print("Row-" + str(index) + " written to DynamoDB successfully")
