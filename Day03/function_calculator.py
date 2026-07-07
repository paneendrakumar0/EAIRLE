def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Function-based Calculator")
    try:
        x = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        y = float(input("Enter second number: "))
        
        if op == '+':
            res = add(x, y)
        elif op == '-':
            res = subtract(x, y)
        elif op == '*':
            res = multiply(x, y)
        elif op == '/':
            res = divide(x, y)
        else:
            res = "Invalid operator"
            
        print(f"Result: {res}")
    except ValueError:
        print("Invalid number input.")

if __name__ == "__main__":
    main()
