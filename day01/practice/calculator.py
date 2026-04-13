# calculator

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number you want to calculate with: "))

choice = input("Enter the choice (+, -, *, /): ")

if choice == "+":
    print ("Addition of ",num1,"and",num2,"is", num1 + num2)
elif choice == "-":
    print ("Substraction of ",num1,"and",num2,"is", num1 - num2)
elif choice == "*":
    print ("Multiplication of ",num1,"and",num2,"is", num1 * num2)
elif choice == "/":
    print ("Division of ",num1,"and",num2,"is", num1 / num2)
elif choice == "%":
    print ("Modulus of ",num1,"and",num2,"is", num1 % num2)
else:
    print("Invalid choice")