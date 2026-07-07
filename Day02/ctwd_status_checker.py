def main():
    try:
        # CTWD: Contact Tip to Work Distance
        ctwd = float(input("Enter CTWD value (in mm): "))
        if ctwd < 10:
            print("Status: Too close")
        elif 10 <= ctwd <= 15:
            print("Status: Ideal")
        else:
            print("Status: Too far")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
