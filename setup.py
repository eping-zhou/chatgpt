import boto3
import json

# AWS credentials and configuration
access_key = "AKIAS2YKINN4UQPCTSMK"
secret_key = "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"
region = "ap-southeast-2"

# Create an AWS session
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)

# Connect to AWS RDS and S3
rds_client = session.client("rds")
s3_client = session.client("s3")

# Save data to AWS RDS
def save_to_rds(data):
    # Code to save data to AWS RDS
    pass

# Save data to AWS S3
def save_to_s3(data):
    bucket_name = "chatgpt-yiping"
    key = "AAPL.json"
    
    # Convert data to JSON string
    json_data = json.dumps(data)
    
    # Upload the JSON data to S3
    s3_client.put_object(Body=json_data, Bucket=bucket_name, Key=key)
    
    print(f"Data saved successfully to S3 bucket: {bucket_name}, key: {key}")

# Read the JSON data file
filename = "AAPL.json"

with open(filename, "r") as file:
    data = json.load(file)

# Call the functions to save data to AWS RDS and S3
save_to_rds(data)
save_to_s3(data)
