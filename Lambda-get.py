from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def lambda_handler(event, context):
    
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table('Dados')

    id = event['pathParameters']['id']

    try:
        response = table.get_item(
            Key={
                'id':id
            }
        )
    except e:
        print(f"error:{e}")
        
   
    if "Item" not in response:
        dados=f'id: {id} nao encontrado'
        res = { "statusCode": '400',
                "body":json.dumps(dados)}
        return res
        
    item = response['Item']
    print(f"item: {item}") 
   
    dados = json.dumps(item, indent=4, cls=DecimalEncoder)
    print(f"Get Item succeeded: {dados}"
    
    res = {"isBase64Encoded": False,
            "statusCode": '200',
            "headers": {},
            "body":dados}
    
    return res