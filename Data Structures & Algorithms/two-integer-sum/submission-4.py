class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in nums and i!=nums.index(complement):
                return sorted([i,nums.index(complement)])
        