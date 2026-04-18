import os
import datetime
import shutil

def backup (source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup{today}" )
    shutil.make_archive(backup_file_name,'gztar', source)

source =  "/mnt/e/DevOps/Python/project"
destination = "/mnt/e/DevOps/Python/project/backup"  

backup (source, destination)