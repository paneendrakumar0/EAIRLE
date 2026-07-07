# DSA Notes - Arrays and Hash Maps

## Two Sum
- **Brute Force Idea**: Use two nested loops to check every possible pair of numbers to see if they sum up to the target.
- **Optimized Idea**: Use a hash map (dictionary in Python) to store the numbers we have seen so far and their indices. For each number, calculate its complement (target - number) and check if the complement is in the hash map.
- **Time Complexity**: 
  - Brute force: O(n^2)
  - Hash map: O(n) - because dictionary lookups take O(1) time on average.
- **Space Complexity**:
  - Brute force: O(1)
  - Hash map: O(n) - in the worst case, we might store all numbers in the dictionary.
- **Edge Case**: The array contains negative numbers, or the target is 0.

## Contains Duplicate
- **Sorting Idea vs Set Idea**: 
  - Sorting Idea: Sort the array first, then iterate through it and check if any adjacent elements are identical.
  - Set Idea: Create a set (hash set) to track the numbers we have seen. If we encounter a number that is already in the set, a duplicate exists.
- **Time Complexity**:
  - Sorting: O(n log n)
  - Set: O(n) on average for hash set lookup and insertion.
- **Space Complexity**:
  - Sorting: O(1) or O(n) depending on the sorting algorithm.
  - Set: O(n) because the set might contain all unique elements.
- **Edge Case**: An empty array or an array with only one element.
