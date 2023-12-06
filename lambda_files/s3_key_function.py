# Step 2: Define the file path within the my-bucket-name S3 bucket:
def lambda_handler(event, context): 
    bucket_name = event["bucket_name"] 
    crash_key = 'crash/crash_data.csv'
    vehicles_key = 'vehicles/vehicles_crash_data.csv'
    people_key = 'people/people_crash_data.csv'  
    return {"bucket_name": bucket_name, "crashes_key": crash_key,
             "vehicles_key": vehicles_key, "people_key": people_key}