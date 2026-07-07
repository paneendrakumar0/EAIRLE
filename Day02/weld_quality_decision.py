def main():
    try:
        travel_speed = float(input("Enter travel speed (mm/s): "))
        work_angle = float(input("Enter work angle (degrees): "))
        ctwd = float(input("Enter CTWD (mm): "))
        
        # Simple decision logic based on some arbitrary optimal thresholds
        score = 0
        if 5 <= travel_speed <= 10:
            score += 1
        if 40 <= work_angle <= 50:
            score += 1
        if 10 <= ctwd <= 15:
            score += 1
            
        if score == 3:
            print("Weld Quality: Good")
        elif score == 2:
            print("Weld Quality: Average")
        else:
            print("Weld Quality: Bad")
            
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
