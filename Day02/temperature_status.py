def main():
    try:
        temp = float(input("Enter temperature (in Celsius): "))
        if temp < 0:
            print("Status: Danger (Freezing)")
        elif temp < 15:
            print("Status: Cold")
        elif temp <= 30:
            print("Status: Normal")
        elif temp <= 50:
            print("Status: Hot")
        else:
            print("Status: Danger (Overheating)")
    except ValueError:
        print("Invalid input: Please enter a numeric value.")

if __name__ == "__main__":
    main()
