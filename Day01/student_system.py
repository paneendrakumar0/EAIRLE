def main():
    print("--- Student Information System ---")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    branch = input("Enter Branch: ")
    semester = input("Enter Semester: ")
    
    print("\n--- Student Summary ---")
    print(f"Name:     {name}")
    print(f"Age:      {age}")
    print(f"Branch:   {branch}")
    print(f"Semester: {semester}")
    print("-----------------------")

if __name__ == "__main__":
    main()
