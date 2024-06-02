import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    source_bucket = event['Records'][0]['s3']['bucket']['name'] ## bucketname
    object_key = event['Records'][0]['s3']['object']['key'] ## filename in the source bucket name
    
    target_bucket = 'copy-of-raw-json-zillow-dataanalysis'
    copy_source = {'Bucket': source_bucket, 'Key':object_key}
    
    waiter = s3_client.get_waiter('object_exists')
    waiter.wait(Bucket=source_bucket, Key=object_key)
    
    s3_client.copy_object(Bucket=target_bucket, Key=object_key, CopySource=copy_source)

    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
