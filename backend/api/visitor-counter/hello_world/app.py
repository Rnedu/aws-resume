import json
import boto3

dynamo_db = boto3.client('dynamodb')
TABLE_NAME = 'VisitorCount'  # Your DynamoDB table name
PRIMARY_KEY = 'PK'           # The primary key for the item
COUNTER_KEY = 'site_visits'  # The counter key in DynamoDB

def lambda_handler(event, context):
    try:
        # Update DynamoDB counter
        response = dynamo_db.update_item(
            TableName=TABLE_NAME,
            Key={
                PRIMARY_KEY: {'S': COUNTER_KEY}  # Use your counter key
            },
            UpdateExpression='SET #count = if_not_exists(#count, :start) + :inc',
            ExpressionAttributeNames={
                '#count': 'count',  # Attribute name for the counter
            },
            ExpressionAttributeValues={
                ':start': {'N': '0'},  # Starting value if it doesn't exist
                ':inc': {'N': '1'},    # Increment value
            },
            ReturnValues='UPDATED_NEW'
        )

        # Return the updated visitor count
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Visitor count updated!',
                'updatedCount': response['Attributes']['count']['N']
            })
        }
    except Exception as e:
        print(f"Error updating counter: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error updating visitor count',
                'error': str(e)
            })
        }
