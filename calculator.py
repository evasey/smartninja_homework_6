number_1 = int(input("Choose your first number: "))

number_2 = int(input("Choose your second number: "))

operator = input("Choose an operator: ")

if operator == "+":
    print(number_1 + number_2)

elif operator == "-":
    print(number_2 - number_2)

elif operator == "*":
    print(number_1 * number_2)

elif operator == "/":
    print(number_1 / number_2)

else:
    print("Error! Please choose a right operator e.g. +, -, *, /")