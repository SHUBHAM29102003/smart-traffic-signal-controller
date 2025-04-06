import json
import random
import datetime
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SmartTrafficData')
sns = boto3.client('sns')

def lambda_handler(event, context):
    traffic_levels = ['LOW', 'MEDIUM', 'HIGH']
    traffic_level = random.choice(traffic_levels)
    timestamp = datetime.datetime.now().isoformat()

    # Save to DynamoDB
    table.put_item(
        Item={
            'timestamp': timestamp,
            'trafficLevel': traffic_level
        }
    )

    # Send alert if traffic is HIGH
    if traffic_level == 'HIGH':
        sns.publish(
            TopicArn='arn:aws:sns:ap-south-1:123456789012:TrafficAlertTopic',
            Message=f'High traffic detected at {timestamp}',
            Subject='Traffic Alert 🚦'
        )

    return {
        'statusCode': 200,
        'body': json.dumps(f'Traffic level {traffic_level} recorded at {timestamp}')
    }

