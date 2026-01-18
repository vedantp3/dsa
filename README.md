# DSA Problem Solutions

A collection of Data Structures and Algorithms problems with solutions and optimized approaches.

---

## Problem Table

| # | Problem Name | Description | Approach | Time Complexity | Space Complexity |
|---|---|---|---|---|---|
| 1 | Count Negative Numbers in a Sorted Matrix | Count the total number of negative numbers in a sorted matrix (rows and columns are sorted in descending order) | Brute Force - Iterate through all elements in the matrix and count negatives | O(m × n) | O(1) |
| 2 | Maximum Count of Positive Integer and Negative Integer | Find the maximum count between positive and negative numbers in a sorted array containing 0s, positive, and negative numbers | Binary Search - Use two binary searches to find the boundary between negatives and positives, then calculate counts and return the maximum | O(log n) | O(1) |

---

## Problem Details

### 1. Count Negative Numbers in a Sorted Matrix
- **Problem Statement:** Given an m × n matrix where each row and column are sorted in descending order, count all negative numbers in the matrix.
- **Approach:** Simple brute force traversal through all matrix elements, checking each for negativity.
- **Optimal Approach:** Could be optimized to O(m + n) by starting from top-right or bottom-left corner.

### 2. Maximum Count of Positive Integer and Negative Integer
- **Problem Statement:** Given a sorted array containing negative numbers, zeros, and positive numbers, return the maximum count between positive and negative integers.
- **Approach:** Perform two binary searches:
  - First binary search finds the first index where element >= 0 (boundary of negatives)
  - Second binary search finds the first index where element > 0 (boundary of positives)
  - Calculate: negative count = firstindex, positive count = n - firstpositive
  - Return the maximum of the two counts
- **Optimization:** Avoids linear scanning by using binary search, reducing time complexity.
