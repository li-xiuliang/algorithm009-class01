class Solution:
    def jump(self, nums: List[int]) -> int:

        end = 1
        start = 0
        res = 0
        while end < len(nums):
            max_pos = 0
            for i in range(start, end):
                max_pos = max(max_pos, nums[i] + i)
            start = end
            end = max_pos + 1
            res += 1
        return res