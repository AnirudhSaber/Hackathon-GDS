import boto3
import random
import datetime
import time


# session = boto3.Session(profile_name='default', region_name='us-east-1')
firehoseClient = boto3.client('firehose',region_name='us-east-1')

def generate_order_data():
    """Generate random order data."""
    ad_id = random.choice([1001, 1002, 1003, 1004, 1005, 1006, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015])
    user_id = random.choice(['U1295','U1296','U1297','U1298','U1299','U1300','U1301','U1302','U1303','U1304','U1305','U1306','U1307','U1308'])
    click_timestamp = datetime.datetime.now().isoformat()
    platform = random.choice(['Mobile','Webpage','DesktopApp','Tablet'])
    location = random.choice(['London','Paris','Uganda','Mumbai','Warangal','Los Angeles'])

    return f'{ad_id},{user_id},{click_timestamp},{platform},{location}\n'


if __name__ == '__main__':
    try:
        while True:
            data = generate_order_data()
            print(data)
            response = firehoseClient.put_record(
                DeliveryStreamName = 'ad-click-stream',
                Record = {
                    'Data': data
                }
            )
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nScript stopped by manual intervention!")