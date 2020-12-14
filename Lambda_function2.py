import boto3
def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CUSTOMERS')
    table.put_item(
        Item = event {
              "CUSTOMER_ID":'1235',
              "CUST_NAME":'PROCOM',
              "LOCATION":'PLATEN'
            
            
        }
                  
                  
)
    
    return {"Code": 200, "message":"Customer Added Successfully"}
