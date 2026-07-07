def main():
    try:
        marks = float(input("Enter marks: "))
        if marks < 0 or marks > 100:
            print("Invalid input: Marks must be between 0 and 100.")
        elif marks >= 90:
            print("Grade: A")
        elif marks >= 80:
            print("Grade: B")
        elif marks >= 70:
            print("Grade: C")
        elif marks >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
    except ValueError:
        print("Invalid input: Please enter a numeric value.")

if __name__ == "__main__":
    main()
