"""
This is a script to take a backup from local to aws s3.
boto3 -> used to do AWS tasks using python. 

"""

import boto3
import os
import datetime
import shutil

s3 = boto3.resource("s3")
def show_bucket(s3):
    print("*** List of current buckets in s3 ***")
    for buckets in s3.buckets.all():
        print(buckets.name)

def create_bucket(s3):
        s3.create_bucket(Bucket="pythonfordevops2609", 
                        CreateBucketConfiguration={
                        'LocationConstraint': 'us-east-2',
                        },)

        print("Bucket has been created successfully.....!!!")
        print("...")

source =  "/mnt/e/DevOps/Python/project"
destination = "/mnt/e/DevOps/Python/project/backup" 

today = datetime.date.today()
backup_file_name = os.path.join(destination,f"backup{today}.tar.gz" )


def backup(source, destination):
    shutil.make_archive(backup_file_name.replace(".tar.gz", " "),'gztar', source) 
    print("Backup has been created successfully.....!!!")
    print("...")


def upload_backup(s3, backup_file_name, bucket_name, key_name):
    data = open(backup_file_name, 'rb') # this will read files in binary
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup has been uploaded successfully.....!!!")
    print("...")

bucket_name ="pythonfordevops2609"
region ="us-east-2"

create_bucket(s3)
backup(source, destination)
upload_backup(s3, backup_file_name, bucket_name,"my_backup.tar.gz")
show_bucket(s3)




    


