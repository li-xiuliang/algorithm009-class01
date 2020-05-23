'''
方法一： 两重循环

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
         for i in range(len(nums) - 1):
             for j in range(i + 1, len(nums)):
                 if nums[i] + nums[j] == target:
                     return [i, j]

'''
方法二： 利用字典简化查找
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         dic_num = {}
         for i in range(len(nums)):
             if target - nums[i] in dic_num:
                 return [i, dic_num[target - nums[i]]]
             dic_num[nums[i]] = i
            