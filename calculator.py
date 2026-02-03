def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Indefinite error"
    else:
        return a / b

def square(a):
    return a * a


print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")

choice = input("Choose the operation (1/2/3/4/5): ")

if choice in ['1', '2', '3', '4']:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(a, b))

elif choice == '2':
    print("Result:", subtract(a, b))

elif choice == '3':
    print("Result:", multiply(a, b))

elif choice =='4':
    print("Result:", divide(a, b))

elif choice == '5':
    a = float(input("Enter the number: "))
    print("Result:", square(a))

else:
    print("Invalid choice")
