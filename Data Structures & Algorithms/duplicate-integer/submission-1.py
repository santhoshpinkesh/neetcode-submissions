class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True

        return False
         