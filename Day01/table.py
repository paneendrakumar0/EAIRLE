def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to print its multiplication table: "))
        print_table(num)
    except ValueError:
        print("Please enter a valid integer.")
