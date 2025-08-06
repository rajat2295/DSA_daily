class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        n=len(nums)
        r=n-1
        
        while l<=r:
            mid = (l+r)//2
            print(l,mid,r,)

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r=mid-1
            else:
                l=mid+1
        return l
