class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out =[]
        n = len(nums)
        nums.sort()
        for i,num in  enumerate(nums):
            if num>0 :
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[left] + nums[right] + num == 0:
                    out.append([num,nums[left],nums[right]])
                    left=left+1
                    right=right-1
 
                    while right>left and nums[right]==nums[right+1]:
                        right = right-1
                    while left < right and nums[left]==nums[left-1]: 
                        left = left+1
                elif nums[left] + nums[right] + num < 0:
                    left = left+1
                else:
                    right-=1

        return(out)
