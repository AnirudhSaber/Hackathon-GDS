import json
import boto3
import io
import pandas as pd

def lambda_handler(event, context):
    
    aws_session = boto3.Session()
    s3client = aws_session.client('s3', region_name="us-east-1")
    dynamodb = aws_session.resource('dynamodb', region_name="us-east-1")
    table = dynamodb.Table('user-demograph')
    
    csv_obj = s3client.get_object(Bucket="user-demograph", Key="user-demographics-data.csv")
    body = csv_obj['Body']
    df = pd.read_csv(io.BytesIO(body.read()))
    
    try:
        with table.batch_writer() as batch:
            for i, row in df.iterrows():
                batch.put_item(Item=row.to_dict())
        print("DynamoDB put_items completed")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")