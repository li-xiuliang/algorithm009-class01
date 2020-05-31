class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
         tempdic = {}

         for i in range(len(nums)):
             if (target - nums[i]) in tempdic:
                 return [tempdic[target - nums[i]], i]
             else:
                 tempdic[nums[i]] = i
         return False