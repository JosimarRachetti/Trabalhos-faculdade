import json
import boto3

def lambda_handler(event, context):
    try:
        id = event["pathParameters"]["id"]
        
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table('Dados')
        
        print(f"info: deletando id {id}")
        response = table.delete_item(Key={
        'id':id})
        
        return {
        'statusCode': 200,
        'body':f'id{id} deletado com sucesso' }
    except Exception as e:
        return {
        'statusCode': 400,
        'error':f"{e}"}
