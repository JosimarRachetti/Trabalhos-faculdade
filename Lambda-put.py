import json
import boto3

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    
    id = event["pathParameters"]["id"]
    
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table('Dados')

   
    try:
        response = table.get_item(
            Key={
                'id': id
            }
        )
        
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'statusCode': 400,
                'body':"error ao recuperar dados"}
    
    
    if not "Item"in response or response['Item'] is None:
        return {'statusCode': 400,
        'body':"error"}


    try:
        item = response['Item']
        dados = json.dumps(item, indent=4, cls=DecimalEncoder)
        dados = json.loads(dados)
        novos_dados = event['body']
        
        novos_dados = json.loads(novos_dados)
        
        dados["nome"] = novos_dados["nome"]
        dados["idade"] = novos_dados["idade"]
        dados["email"] = novos_dados["email"]
        dados["telefone"] = novos_dados["telefone"]
        
        print(f"info: atualizando dados {dados}")
        table.put_item(Item=dados)
        
        return {
            'statusCode': 200,
            'body':f"dados:{dados}"}
    except:
        return {
            'statusCode': 400,
            'body':f"error: erro ao atualizar dados"}