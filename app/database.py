import boto3

def get_dynamodb_resource():
    return boto3.resource('dynamodb', region_name='eu-central-1')
