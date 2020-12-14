import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CUSTOMERS')
   
def lambda_handler2(event, context): 
   table.put_item(Item = event, Key={'CUSTOMER_ID':{'S':str("VALUE")}})            
    
   return {"Status_code" : 200, "message" : "Customer Added Successfully"}

