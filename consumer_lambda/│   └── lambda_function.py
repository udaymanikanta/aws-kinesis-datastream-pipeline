import json
import base64

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            payload = base64.b64decode(record['kinesis']['data'])
            data = json.loads(payload)

            print("Processed Record:")
            print(f"Bucket: {data['bucket']}")
            print(f"File Name: {data['file_name']}")

        return {
            'statusCode': 200,
            'body': json.dumps('Records processed successfully!')
        }

    except Exception as e:
        print("Error:", str(e))
        raise e
