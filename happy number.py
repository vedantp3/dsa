from typing import Set
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n = self.sumofsquare(n)
        return True
    def sumofsquare(self, n:int):
        s = 0
        while n>0:
            digit = n%10
            s += digit*digit
            n//= 10
        return s
    
