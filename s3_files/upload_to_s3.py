# import pandas as pd
# # Step 1: Read in Data
# crashes_df = pd.read_csv('crash_data.csv')
# vehicles_df = pd.read_csv('vehicle_crash_data.csv')
# people_df= pd.read_csv('people_crash_data.csv')

# # Step 2: Filter dataframes by column lists
# filtered_crashes_df = crashes_df[['crash_record_id', 'posted_speed_limit', 'crash_date']]
# filtered_vehicles_df = vehicles_df[['vehicle_id', 'make', 'model', 'vehicle_year', 'type']]
# filtered_people_df = people_df[['person_id', 'crash_id', 'crash_date', 'PERSON_TYPE', 'vehicle_id', 'sex',
# 'age']]

# # Step 3: Place transformed data in dictionary for output
# transformed_content = {
# 'crashes_df': filtered_crashes_df.to_csv(index=False),
# 'vehicles_df': filtered_vehicles_df.to_csv(index=False),
# 'people_df': filtered_people_df.to_csv(index=False)
# }

import boto3
import pandas as pd

# Step 1: Establish the boto3 s3 Client
s3 = boto3.client('s3')
bucket_name = 'koks-aws-bucket'

# Step 2: Define file paths within your local environment
crash_path = './data/crash_data.csv'
vehicles_path = './data/vehicle_crash_data.csv'
people_path= './data/people_crash_data.csv'

# Step 3: Define output file paths within "my-bucket-name" s3 bucket in a 'traffic' directory
crash_key = 'crash/crash_data.csv'
vehicles_key = 'vehicles/vehicles_crash_data.csv'
people_key = 'people/people_crash_data.csv'

# upload the file
crash_response = s3.upload_file(Filename=crash_path, Bucket=bucket_name, Key=crash_key)

vehicles_response = s3.upload_file(Filename=vehicles_path, Bucket=bucket_name, Key=vehicles_key)

people_response = s3.upload_file(Filename=people_path, Bucket=bucket_name, Key=people_key)


# # Step 1: Establish the boto3 s3 Client
# def lambda_handler(event, context): 
#     s3 = boto3.client('s3') 
#     return {"s3": s3, "bucket_name": 'koks-aws-bucket'}

# # Step 2: Define the file path within the my-bucket-name S3 bucket:
# def lambda_handler(event, context): 
#     bucket_name = event["bucket_name"] 
#     crash_key = 'crash/crash_data.csv'
#     vehicles_key = 'vehicles/vehicles_crash_data.csv'
#     people_key = 'people/people_crash_data.csv'  
#     return {"bucket_name": bucket_name, "crashes_key": crash_key,
#              "vehicles_key": vehicles_key, "people_key": people_key}

# # Step 3: Use s3.get_object() to reference the file object in the S3 bucket:
# def lambda_handler(event, context): 
#     s3 = boto3.client('s3') 
#     bucket_name = event["bucket_name"] 
#     crash_key = event["crash_key"]
#     vehicles_key = event["vehicles_key"]
#     people_key = event["people_key"] 

#     crash_response = s3.get_object(Bucket=bucket_name, Key=crash_key) 
#     vehicles_response = s3.get_object(Bucket=bucket_name, Key=vehicles_key) 
#     people_response = s3.get_object(Bucket=bucket_name, Key=people_key) 
#     return {"crash_response": crash_response, "vehicles_response":vehicles_response, 
#             "people_response": people_response}