class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num
        while l<=r:
            m = (l+r)//2
            ms= m*m
            if ms == num:
                return True
            elif ms < num:
                l=m+1
            else:
                r=m-1
        return False
