class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(path, check):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                dfs(path + [nums[i]], check)
                check[i] = 0
        res = []
        check = [0] * len(nums)
        nums.sort()
        dfs([],check)
        return res