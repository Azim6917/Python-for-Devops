"""
This is a script to take a backup from local to aws s3.
boto3 -> used to do AWS tasks using python. 

"""

import boto3

s3 = boto3.resource("s3")
def show_bucket(s3):
    for buckets in s3.buckets.all():
        print(buckets.name)

def create_bucket(s3):
    s3.create_bucket(Bucket="python769245602", 
                    CreateBucketConfiguration={
                    'LocationConstraint': 'us-east-2',
                    },)

create_bucket(s3)
show_bucket(s3)

    

