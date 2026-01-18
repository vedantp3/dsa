class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        prime = [2,3,5]
    
        for i in range(len(prime)):
            while n%prime[i] == 0:
                n = n/prime[i]
        return n == 1  

        # time = O(logn)
        #space = O(1)  
        


        
        