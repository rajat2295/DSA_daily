# import Math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_min(k):
            hours =0
            for p in piles:
                hours+= math.ceil(p/k)
            return hours <=h
        l = 1
        r = max(piles)
        while l<r:
            m = (l+r)//2
            if k_min(m):
                r= m
            else:
                l=m+1
        return r
