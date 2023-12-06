import boto3

# Step 1: Establish the boto3 s3 Client
def lambda_handler(event, context): 
    s3 = boto3.client('s3') 
    return {"s3": s3, "bucket_name": 'koks-aws-bucket'}
