class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        out = 0
        for num in num_set:
            if num-1 not in num_set:
                next = num+1
                while next in num_set:
                    next+=1
                out = max(out,next-num)
        return out 
