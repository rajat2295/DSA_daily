class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        cnt = 0
        for c in stones:
            if c in jewels:
                cnt += 1
        return cnt
