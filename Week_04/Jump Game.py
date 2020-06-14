class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        rightmost = 0

        for i in range(len(nums)):
            if i <= rightmost:
                rightmost = max(nums[i] + i, rightmost)
            if rightmost >= len(nums) - 1:
                return True
        return False