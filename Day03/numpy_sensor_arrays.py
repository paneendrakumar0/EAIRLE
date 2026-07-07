import numpy as np

def main():
    # 1. Array of 10 mock distance sensor readings
    readings = np.array([0.32, 0.35, 0.31, 0.40, 0.38, 0.36, 0.33, 0.39, 0.41, 0.37])
    print("--- 1D Sensor Readings ---")
    print(f"Shape: {readings.shape}")
    print(f"NDim: {readings.ndim}")
    print(f"Size: {readings.size}")
    print(f"DType: {readings.dtype}")
    print(f"Mean: {readings.mean():.3f}, Min: {readings.min()}, Max: {readings.max()}\n")

    # 2. 2D array of 5 robot poses (x, y, theta)
    poses = np.array([
        [0.0, 0.0, 0.0],
        [1.0, 0.5, 0.2],
        [2.0, 1.0, 0.4],
        [3.0, 1.5, 0.6],
        [4.0, 2.0, 0.8]
    ])
    print("--- 2D Robot Poses ---")
    print(f"First pose: {poses[0]}")
    print(f"Last pose: {poses[-1]}")
    print(f"Mean x position: {poses[:, 0].mean()}")
    print(f"Mean y position: {poses[:, 1].mean()}\n")
    
    # 3. Why NumPy helps AI/Robotics
    print("--- Why NumPy? ---")
    print("# TODO: Write your 5 lines explaining why NumPy helps AI/robotics here!")
    print("# 1.")
    print("# 2.")
    print("# 3.")
    print("# 4.")
    print("# 5.")

if __name__ == "__main__":
    main()
