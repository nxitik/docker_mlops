import boto3
import pandas as pd
from secret_keys import *
import os
os.environ["AWS_DEFAULT_REGION"] = 'us-east-2'
os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key_id
os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key
subfolder = 'Data_extract_from_s3'
original_directory = os.getcwd()
new_directory = os.path.join(original_directory, subfolder)
os.chdir(new_directory)
# os.chdir(r'C:\Users\Naitik\OneDrive\Desktop\Masters\Docker_MLOPS\Data_extract_from_s3')
print(os.getcwd())
s3 = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

obj = s3.Bucket('naitiktest').Object('healthcare_dataset.csv').get()
df = pd.read_csv(obj['Body'], index_col=0)



df.to_csv('healthcare_dataset.csv')