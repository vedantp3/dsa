# DSA Problem Solutions

A collection of Data Structures and Algorithms problems with solutions and optimized approaches.

---

## Problem Table

| # | Problem Name | Description | Approach | Time Complexity | Space Complexity |
|---|---|---|---|---|---|
| 1 | Count Negative Numbers in a Sorted Matrix | Count the total number of negative numbers in a sorted matrix (rows and columns are sorted in descending order) | Brute Force - Iterate through all elements in the matrix and count negatives | O(m × n) | O(1) |
| 2 | Maximum Count of Positive Integer and Negative Integer | Find the maximum count between positive and negative numbers in a sorted array containing 0s, positive, and negative numbers | Binary Search - Use two binary searches to find the boundary between negatives and positives, then calculate counts and return the maximum | O(log n) | O(1) |
| 3 | Happy Number | Determine if a number is a happy number (repeatedly replace the number by the sum of squares of its digits until it becomes 1 or enters a cycle) | Hash Set with Cycle Detection - Track seen numbers and repeatedly calculate sum of squares of digits; return True if reaches 1, False if cycle detected | O(log n) | O(1) |
| 4 | Ugly Number | Determine if a number is an ugly number (has only prime factors 2, 3, and 5) | Prime Factorization - Divide the number by 2, 3, and 5 repeatedly; if result is 1, it's an ugly number | O(log n) | O(1) |

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

### 3. Happy Number
- **Problem Statement:** Determine if a number is a "happy number". A happy number is defined by repeating the process of replacing the number by the sum of squares of its digits. If the process eventually reaches 1, the number is happy. If it loops endlessly in a cycle that doesn't include 1, it's not happy.
- **Approach:** Use a Hash Set to detect cycles:
  - Maintain a set of numbers we've seen during the process
  - Repeatedly calculate the sum of squares of digits
  - If we reach 1, return True (happy number)
  - If we encounter a number already in the set, we've found a cycle, return False
  - Use a helper function `sumofsquare()` to calculate the sum of squares of digits
- **Optimization:** Hash set ensures O(1) lookup to detect cycles efficiently.

### 4. Ugly Number
- **Problem Statement:** Determine if a number is an "ugly number". An ugly number is a positive integer whose prime factors are only 2, 3, and 5.
- **Approach:** Prime Factorization:
  - Check if the number is positive; if not, return False
  - Define the list of prime factors: [2, 3, 5]
  - For each prime factor, repeatedly divide the number by it while the division is even (no remainder)
  - After processing all prime factors, if the result is 1, then the number only has 2, 3, and 5 as prime factors (ugly number)
  - If the result is not 1, the number has other prime factors and is not ugly
- **Optimization:** Time complexity is O(log n) since we're dividing the number repeatedly. Space complexity is O(1) as we only use a constant amount of extra space.
