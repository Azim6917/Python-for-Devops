import subprocess

def terraform_run(command):
    subprocess.run(command, shell=True, check=True) 

directory = "E:/DevOps/Python/project/terraform_automate/Wanderlust-Mega-Project-main/terraform"
# command = f"terraform -chdir={directory} init"
command = f"terraform -chdir={directory} destroy -auto-approve"


terraform_run(command)