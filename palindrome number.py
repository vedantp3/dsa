class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s= str(x)

        mid = len(s)//2
        first = s[:mid]
        if len(s)%2 == 0:
            last = s[mid:]
        else:
            last = s[mid+1:]

        return first == last[::-1]



    