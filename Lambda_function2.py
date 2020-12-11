import boto3, json
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CUSTOMERS")
from boto3.dynamodb.conditions import Key, Attr
def lambda_handler2(event, context):
    table.put_item(Item=event)
    return {"code":200, "message":"Customer Added Successfully"}
