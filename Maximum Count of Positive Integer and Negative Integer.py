from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        l,r = 0, n-1
        firstindex = n
        while l<=r:
            mid = (l+r)//2
            if nums[mid] >= 0:
                firstindex = mid
                r = mid -1 
            else:
                l = mid + 1
        
        l, r = 0, n-1
        firstpositive = n
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > 0:
                firstpositive = mid
                r = mid -1
            else:
                l = mid+1
        negative = firstindex
        positive = n - firstpositive
        return max(negative, positive)

        #time = O()
