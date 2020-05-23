class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        before_zero = 0

        for after_zero in range(len(nums)):

            if nums[after_zero] != 0:
                nums[before_zero], nums[after_zero] = nums[after_zero], nums[before_zero]
                before_zero += 1
                