from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        i = m-1
        j=0
        while i>=0 and j<n:
            if grid[i][j] < 0:
                count += (n-j)
                i -=1
            else:
                j+=1
        return count
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] < 0:
        #             count+=1
        # return count

        #time complexit = O(mxn)
        #sapce complexity = O(1)

        