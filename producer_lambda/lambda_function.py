import json
import boto3
import os

kinesis_client = boto3.client('kinesis')
STREAM_NAME = os.environ.get('STREAM_NAME', 'file-metadata-stream')

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            
            metadata = {
                "bucket": bucket,
                "file_name": key
            }

            kinesis_client.put_record(
                StreamName=STREAM_NAME,
                Data=json.dumps(metadata),
                PartitionKey=key
            )

        return {
            'statusCode': 200,
            'body': json.dumps('Metadata sent to Kinesis successfully!')
        }

    except Exception as e:
        print("Error:", str(e))
        raise e
