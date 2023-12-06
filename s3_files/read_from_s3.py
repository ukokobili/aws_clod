import boto3
import pandas as pd

# Step 1: Establish the boto3 s3 Client
s3 = boto3.client('s3')
bucket_name = 'koks-aws-bucket'

# Step 2: Define file path within "my-bucket-name" s3 bucket
crash_key = 'crash/crash_data.csv'
vehicles_key = 'vehicles/vehicles_crash_data.csv'
people_key = 'people/people_crash_data.csv'

# Step 3: Use s3.get_object() to reference the file "object" in the s3 bucket
crash_response = s3.get_object(Bucket=bucket_name, Key=crash_key)
vehicles_response = s3.get_object(Bucket=bucket_name, Key=vehicles_key)
people_response = s3.get_object(Bucket=bucket_name, Key=people_key)

# Step 4: Read in Data
crash_df = pd.read_csv(crash_response['Body'])
vehicles_df = pd.read_csv(vehicles_response['Body'])
people_df = pd.read_csv(people_response['Body'])

print(crash_df)
