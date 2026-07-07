import time

def simulate_drain(start_percentage, drain_rate):
    current = start_percentage
    step = 0
    while current > 10:
        print(f"Step {step}: Battery at {current:.1f}%")
        current -= drain_rate
        step += 1
        time.sleep(0.1) # Simulate time passing
    print(f"Step {step}: Battery CRITICAL at {current:.1f}%! Please recharge.")

def main():
    try:
        start = float(input("Enter starting battery percentage: "))
        rate = float(input("Enter drain rate per step: "))
        if start > 0 and rate > 0:
            simulate_drain(start, rate)
        else:
            print("Values must be positive.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
