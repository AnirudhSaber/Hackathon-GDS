import boto3
import base64
import json
from decimal import Decimal

def lambda_handler(event, context):

    records = event.get("Records")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("ad-click-conversion")

    for record in records:

        payload=base64.b64decode(record["kinesis"]["data"])
        dict = json.loads(payload)
        ad_id = dict['ad_id']
        user_id = dict['user_id']
        dict['revenue'] = Decimal(dict['revenue'])

        clickItem = table.get_item(Key={'ad_id': ad_id, 'user_id': user_id})
        dict['gender'] = clickItem["Item"]["gender"]
        dict['interests'] = clickItem["Item"]["interests"]
        dict['age'] = int(clickItem["Item"]["age"])
        dict['campaign'] = clickItem["Item"]["campaign"]
        dict['product'] = clickItem["Item"]["product"]
        dict['target_end_date'] = clickItem["Item"]["target_end_date"]
        dict['target_start_date'] = clickItem["Item"]["target_start_date"]
        print(dict)
        response = table.put_item( Item=dict )
        print(response)