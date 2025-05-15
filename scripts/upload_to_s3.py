from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET_NAME
import boto3
from botocore.exceptions import NoCredentialsError

file_path = 'results/top_reviewed_products.csv'
s3_file_name = 'top_reviewed_products.csv' 

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def upload_to_s3(file_path, bucket_name, s3_file_name):
    try:
        s3.upload_file(file_path, bucket_name, s3_file_name)
        print(f"Successfully uploaded {file_path} to S3 bucket '{bucket_name}' as '{s3_file_name}'")
    except FileNotFoundError:
        print("File not found.")
    except NoCredentialsError:
        print("Credentials not available.")

upload_to_s3(file_path, BUCKET_NAME, s3_file_name)