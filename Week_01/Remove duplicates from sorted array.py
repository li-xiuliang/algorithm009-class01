class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                if i - count > 1:
                    nums[count + 1] = nums[i]
                count += 1
        return count + 1