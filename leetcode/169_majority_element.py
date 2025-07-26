class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for num in counter:
            if counter[num] > len(nums)//2:
                return num
