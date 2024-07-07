#function to add two numbers
def add(x1,x2):
    return x1 + x2
#function to subtract two numbers
def sub(x1,x2):
    return x1 - x2 
#function to multiply two numbers
def multiply(x1,x2):
    return x1 * x2
#function to divide two  numbers
def divide(x1,x2):
    return x1 / x2
print("Please select the operation -\n"\
    "1. Add\n"\
    "2. Sub\n"\
    "3. Multiply\n"\
    "4. Divide\n")
#Taking the input from the user
select = int(input(" Select Operations from 1, 2, 3, 4:"))
number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))
if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=", sub(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
else:
    print("invalid input")

