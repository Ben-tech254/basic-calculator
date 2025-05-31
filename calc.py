#Function to add two numbers
def add(x, y):
    return x + y

#Function to subtract two numbers
def subtract(x, y):
    return x - y

#Function to multiply two numbers
def multiply(x, y):
    return x * y

#Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed"
    else:
        return x / y

def calculator():
    print('Arithmetic operations')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')

    while True:
        operation = input("Enter the operation (1/2/3/4): ")
        if operation in ['1', '2', '3', '4']:
            num1 = float(input("Input the first number: "))
            num2 = float(input("Input the second number: "))
            if operation == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid operation. Please try again.")

        # Ask if the user wants to perform another calculation
            
        continuity = input("Do you want to perform another calculation? (yes/no)")
        if continuity.lower() != 'yes':
                break
    print("Exiting the calculator!, Goodbye")

calculator()