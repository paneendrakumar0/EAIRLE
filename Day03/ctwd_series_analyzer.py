def analyze_ctwd(ctwd_list):
    ideal_count = 0
    for val in ctwd_list:
        if 10 <= val <= 15:
            ideal_count += 1
    return ideal_count

def main():
    # Pre-defined list for demonstration, or we can take input
    ctwd_values = [9.5, 12.0, 14.5, 16.2, 11.1, 10.5, 8.0]
    print(f"Analyzing CTWD values: {ctwd_values}")
    
    ideal = analyze_ctwd(ctwd_values)
    total = len(ctwd_values)
    print(f"Ideal readings: {ideal} out of {total}")
    print(f"Ideal percentage: {(ideal/total)*100:.1f}%")

if __name__ == "__main__":
    main()
