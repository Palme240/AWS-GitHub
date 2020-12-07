import json


def lambda_handler(event, context):
    return response("Welcome to my python lambda function", 200)


def response(message, status_code):
    return {
        'isBase64Encoded': False,
        'statusCode': status_code,
        'body': json.dumps(message),
        'headers': {'Content-Type': 'application/json'}
    }
