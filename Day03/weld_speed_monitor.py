def count_speeds(speeds):
    slow, good, fast = 0, 0, 0
    for speed in speeds:
        if speed < 5:
            slow += 1
        elif 5 <= speed <= 10:
            good += 1
        else:
            fast += 1
    return slow, good, fast

def main():
    speeds = []
    print("Enter weld speeds (type 'done' when finished):")
    while True:
        val = input("> ")
        if val.lower() == 'done':
            break
        try:
            speeds.append(float(val))
        except ValueError:
            print("Invalid number.")
            
    slow, good, fast = count_speeds(speeds)
    print(f"\nSummary of {len(speeds)} readings:")
    print(f"Slow: {slow} | Good: {good} | Fast: {fast}")

if __name__ == "__main__":
    main()
