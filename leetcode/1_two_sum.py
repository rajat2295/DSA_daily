class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic ={}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in dic and dic[remainder]!=i:
                return [i,dic[remainder]]
