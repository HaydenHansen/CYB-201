#Making a mini calc
#Hayden Hansen, Jan 20, 2021

#add
def add(x, y):
    return x + y

#subtract
def subtract(x, y):
    return x - 7

#multiplication
def multiplication(x, y):
    return x * y

#division
def division(x, y):
    return x / y

print("select operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
#take inpout from the user
while True:
    choice = input("enter choice(1/2/3/4): ")

    # check if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("please input the first number: "))
        num2 = float(input("please input the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        break
    else:
        print("Invalid Input")

    
