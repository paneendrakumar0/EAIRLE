def main():
    try:
        battery = float(input("Enter battery percentage: "))
        if battery < 0 or battery > 100:
            print("Invalid battery percentage.")
        elif battery <= 10:
            print("Status: Critical")
        elif battery <= 30:
            print("Status: Low")
        elif battery < 95:
            print("Status: Normal")
        else:
            print("Status: Full")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
