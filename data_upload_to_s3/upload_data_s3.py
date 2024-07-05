import boto3
import pandas as pd
from secret_keys import *
import os
os.environ["AWS_DEFAULT_REGION"] = 'us-east-2'
os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key_id
os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key
# os.chdir(r'C:\Users\Naitik\OneDrive\Desktop\Masters\Docker_MLOPS\Data_upload_to_s3')
subfolder = 'Data_upload_to_s3'
original_directory = os.getcwd()
new_directory = os.path.join(original_directory, subfolder)
os.chdir(new_directory)
print(os.getcwd())
s3 = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

for bucket in s3.buckets.all():
    print(bucket.name)

# s3.Bucket('naitiktest').upload_file(Filename='BankNote_Authentication.csv', Key='BankNote_Authentication.csv')
s3.Bucket('naitiktest').upload_file(Filename='healthcare_dataset.csv', Key='healthcare_dataset.csv')
for obj in s3.Bucket('naitiktest').objects.all():
    print(obj)