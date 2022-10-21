# building a better calculator

# num1 = float(input("Enter number 1: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter number 2: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/" :
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")


num1 = float(input("Enter number 1: "))
op = input("Enter operator: ")
# if op != "+":
#     print("Invalid operator")
# elif op != "-":
#     print("Invalid operator")
# elif op != "/":
#     print("Invalid operator")
# elif op != "*":
#     print("Invalid operator")
# else:
#     print("Continue operation")

num2 = float(input("Enter number 2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operation")