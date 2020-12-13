import boto3

def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    PARTTION_KEY = 'CUSTOMER_ID'
    table.put_item(
    Item={
        PARTITION_KEY: {'S': 'my-part-key'}
    }
)
    return {"Code": 200, "message":"Customer Added Successfully"}
