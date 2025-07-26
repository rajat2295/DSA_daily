class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        out = []
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                out.append(pow(nums[left],2))
                left+=1
            else:
                out.append(pow(nums[right],2))
                right-=1
        return ((out[::-1]))
