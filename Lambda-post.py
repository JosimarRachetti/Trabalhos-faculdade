import boto3
import json
import decimal
import uuid
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    try:   
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Dados')
        print(f'info: event {event}')
        body = event['body']
        
        body = json.loads(body)
        cadastro = dict()
        cadastro["id"]=str(uuid.uuid4())
        cadastro["data"] = datetime.now().isoformat()
        cadastro["email"]=body["email"]
        cadastro["nome"]=body["nome"]
        cadastro["telefone"]=body["telefone"]
        cadastro["idade"]=body["idade"]
        
        
        print(f'info: cadastro {cadastro}')
        table.put_item(
            Item=cadastro)
            
        print(f'info: sucesso cadastro')
        return  {
            "isBase64Encoded": False,
            "statusCode": '200',
            "headers": {},
            "body": f'message: id {cadastro["id"]} salvo'}
            
    except Exception as e:
        print(f'error: {e}')
        return  {
            "isBase64Encoded": False,
            "statusCode": '400',
            "headers": {},
            "body": f'error:{e}'}