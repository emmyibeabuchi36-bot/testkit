# STAGE ONE
calc_name ="IEM lite"
print("welcome, I am ",calc_name,"\nlet me handle the calculations.")
print()
# STAGE TWO
print("Menu")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("5: FloorDivision")
print("6: Esponential")
print("7: Modulus")

print()

print("Select an operation")
choice = input("Enter a number (1-4):")
print()
# STAGE THREE (DISCISION MAKE)
if choice == "1":
    num1 = input("Enter num1: ")
    num1 = float(num1)
    num2 = input("Enter num2: ")
    num2 = float(num2)
    result = num1 + num2
    print("result =", result)
elif choice == "2":
    num1 = input("Enter num1: ")
    num1 = float(num1)
    num2 = input("Enter num2: ")
    num2 = float(num2)
    result = num1 - num2
    print("result =", result)   
elif choice == "3":
    num1 = input("Enter num1: ")
    num1 = float(num1)
    num2 = input("Enter num2: ")
    num2 = float(num2)
    result = num1 * num2
    print("result =", result) 
elif choice == "4":
    num1 = input("Enter num1: ")
    num1 = float(num1)
    num2 = input("Enter num2: ")
    num2 = float(num2)
    result = num1 / num2
    print("result =", result)  
elif choice == "5":
    num1 = input("Enter num1: ")
    num1 = float(num1)
    num2 = input("Enter num2: ")
    num2 = float(num2)
    result = num1 // num2
    print("result =", result)   
elif choice == "6":
    num1 = input("Enter num1: ")
    num1 = float(num1)
    num2 = input("Enter num2: ")
    num2 = float(num2)
    result = num1 ** num2
    print("result =", result) 
elif choice == "7":
    num1 = input("Enter num1: ")
    num1 = float(num1)
    num2 = input("Enter num2: ")
    num2 = float(num2)
    result = num1 % num2
    print("result =", result)  
# elif choice == "8":
#     num1 = input("Enter num1: ")
#     num1 = float(num1)
#     num2 = input("Enter num2: ")
#     num2 = float(num2)
#     result = num1 math.log(10) num2
    print("result =", result)               
else:
    print("Entery is invalid")          






