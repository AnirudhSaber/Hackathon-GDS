import boto3
import base64
import json

def lambda_handler(event, context):

    records = event.get("Records")
    dynamodb = boto3.client('dynamodb')

    for record in records:

        payload=base64.b64decode(record["kinesis"]["data"])
        dict = json.loads(payload)
        ad_id = str(dict['ad_id'])
        user_id = dict['user_id']

        clickItem = dynamodb.get_item(TableName='ad-click-conversion', Key={'user_id':{'S':user_id},'ad_id':{'N':ad_id}})
        dict['conversion_timestamp'] = clickItem["Item"]["conversion_timestamp"]["S"]
        dict['product_id'] = clickItem["Item"]["product_id"]["S"]
        dict['revenue'] = str(clickItem["Item"]["revenue"]["N"])

        response = dynamodb.put_item(TableName='ad-click-conversion', 
                        Item={'ad_id':{'N':ad_id},
                                'user_id':{'S':user_id},
                                'gender':{'S':dict['gender']},
                                'interests':{'S':dict['interests']},
                                'age':{'N':dict['age']},
                                'campaign':{'S':dict['campaign']},
                                'product':{'S':dict['product']},
                                'target_end_date':{'S':dict['target_end_date']},
                                'target_start_date':{'S':dict['target_start_date']},
                                'revenue':{'N':dict['revenue']},
                                'product_id':{'S':dict['product_id']},
                                'conversion_timestamp':{'S':dict['conversion_timestamp']},
                        })