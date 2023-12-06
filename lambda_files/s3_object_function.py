import boto3

# Step 3: Use s3.get_object() to reference the file object in the S3 bucket:
def lambda_handler(event, context): 
    s3 = boto3.client('s3') 
    bucket_name = event["bucket_name"] 
    crash_key = event["crash_key"]
    vehicles_key = event["vehicles_key"]
    people_key = event["people_key"] 