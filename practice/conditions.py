#if else condition program.

env = input("Enter the stages 'stg''prod''test' ")

if env == "prod":
    print("....Dont Deploy....")
elif env == "stg":
    print("take backup and test well")
else:
    print("Deploy anyday")