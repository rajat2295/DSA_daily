class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = n//2
        first = 0
        last = n-1
        while first<=last:
            mid = (first+last) //2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                last = mid-1
            else:
                first= mid+1
        return -1   
