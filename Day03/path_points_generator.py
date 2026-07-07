def generate_straight_line(start_x, start_y, end_x, end_y, steps):
    points = []
    dx = (end_x - start_x) / steps
    dy = (end_y - start_y) / steps
    
    for i in range(steps + 1):
        x = start_x + (dx * i)
        y = start_y + (dy * i)
        points.append((x, y))
    return points

def main():
    print("Generating robot path points...")
    path = generate_straight_line(0, 0, 10, 5, steps=5)
    
    for i, point in enumerate(path):
        print(f"Waypoint {i}: x={point[0]:.2f}, y={point[1]:.2f}")

if __name__ == "__main__":
    main()
