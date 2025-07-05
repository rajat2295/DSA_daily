class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1]*n
        prefix_prod = 1
        suffix_prod = 1
        for j in range(n):
            out[j] = prefix_prod* out[j]
            prefix_prod = prefix_prod * nums[j]
        for j in range(n-1,-1,-1):
            out[j] = out[j]*suffix_prod
            suffix_prod = nums[j] * suffix_prod    

        return out
