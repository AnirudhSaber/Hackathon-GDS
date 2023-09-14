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
        
        userItem = dynamodb.get_item(TableName='user-demograph', Key={'user_id':{'S':user_id}})
        dict['gender'] = userItem["Item"]["gender"]["S"]
        dict['interests'] = userItem["Item"]["interests"]["S"]
        dict['age'] = str(userItem["Item"]["age"]["N"])
        
        campaignItem = dynamodb.get_item(TableName='campaigns', Key={'ad_id':{'N':ad_id}})
        dict['campaign'] = campaignItem["Item"]["campaign"]["S"]
        dict['product'] = campaignItem["Item"]["product"]["S"]
        dict['target_end_date'] = campaignItem["Item"]["target_end_date"]["S"]
        dict['target_start_date'] = campaignItem["Item"]["target_start_date"]["S"]

        
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
                                
                        })
        print(response)