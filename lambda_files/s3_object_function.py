import boto3

# Step 3: Use s3.get_object() to reference the file object in the S3 bucket:
def lambda_handler(event, context): 
    s3 = boto3.client('s3') 
    bucket_name = event["bucket_name"] 
    crash_key = event["crash_key"]
    vehicles_key = event["vehicles_key"]
    people_key = event["people_key"] 

    crash_response = s3.get_object(Bucket=bucket_name, Key=crash_key) 
    vehicles_response = s3.get_object(Bucket=bucket_name, Key=vehicles_key) 
    people_response = s3.get_object(Bucket=bucket_name, Key=people_key) 
    
    # Step 4: Extract data from each response and store it as a list of dictionaries for further processing:
    return {"crash_response": crash_response, "vehicles_response":vehicles_response, 
            "people_response": people_response}