# Addition
def add(a, b):
    return a + b
# Subtraction
def subtract(a, b):
    return a - b
# Multiply
def multiply(a, b):
    return a * b
# Divide
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
# Gets the user input
def get_user_input():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Please enter valid numbers")
        return get_user_input()

def main():
    print("Select any operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("Enter operation as either (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting calculator...")
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input! Please try again.")
            continue
        
        num1, num2 = get_user_input()
        
        try:
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        except ValueError as e:
            print(f"Error: {e}")
        
        print() 

if __name__ == "__main__":
    main()