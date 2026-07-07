def analyze_sensors(readings):
    if not readings:
        return 0, 0, 0
    return sum(readings) / len(readings), min(readings), max(readings)

def main():
    readings = []
    while True:
        val = input("Enter sensor reading (or 'q' to quit): ")
        if val.lower() == 'q':
            break
        try:
            readings.append(float(val))
        except ValueError:
            print("Please enter a valid number.")
    
    if readings:
        avg_val, min_val, max_val = analyze_sensors(readings)
        print(f"\nReadings: {readings}")
        print(f"Average: {avg_val:.2f}, Min: {min_val:.2f}, Max: {max_val:.2f}")
    else:
        print("No readings entered.")

if __name__ == "__main__":
    main()
