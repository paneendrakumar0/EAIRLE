def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        fact = factorial(num)
        if fact is not None:
            print(f"The factorial of {num} is {fact}")
        else:
            print("Factorial is not defined for negative numbers.")
    except ValueError:
        print("Please enter a valid integer.")
