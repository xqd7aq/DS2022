#!/usr/bin/env python3

import os
import boto3
import requests

# Variables
BUCKET_NAME = "ds2022-xqd7aq"
FILE_URL = "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"  # Example GIF URL
FILE_NAME = "file.gif"
AWS_REGION = "us-east-1"
EXPIRATION = 604800  # 7 days in seconds

# Fetch the file from the internet
def fetch_file(url, file_name):
    print("Fetching file from URL...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {file_name}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        exit(1)

# Upload the file to S3
def upload_to_s3(bucket_name, file_name, region):
    print("Uploading file to S3 bucket...")
    s3_client = boto3.client('s3', region_name=region)
    try:
        s3_client.upload_file(file_name, bucket_name, file_name)
        print(f"File uploaded to S3 bucket: {bucket_name}/{file_name}")
    except Exception as e:
        print(f"Failed to upload file to S3: {e}")
        exit(1)

# Generate a presigned URL for the file
def generate_presigned_url(bucket_name, object_name, expires_in, region):
    print("Generating presigned URL...")
    s3_client = boto3.client('s3', region_name=region)
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expires_in
        )
        return response
    except Exception as e:
        print(f"Failed to generate presigned URL: {e}")
        exit(1)

# Main script execution
if __name__ == "__main__":
    # Fetch and save the file
    fetch_file(FILE_URL, FILE_NAME)

    # Upload the file to S3
    upload_to_s3(BUCKET_NAME, FILE_NAME, AWS_REGION)

    # Generate the presigned URL
    presigned_url = generate_presigned_url(BUCKET_NAME, FILE_NAME, EXPIRATION, AWS_REGION)
    print(f"Presigned URL: {presigned_url}")

    # Optional: Write the presigned URL to a file for submission
    with open("presigned_url.txt", "w") as f:
        f.write(f"Presigned URL: {presigned_url}\n")

