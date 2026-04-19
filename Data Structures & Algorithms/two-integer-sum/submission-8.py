class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        exists={}

        for index,number in enumerate(nums):
            diff=target-number

            if diff in exists:
                return [exists[diff],index]

            exists[number]=index

        
