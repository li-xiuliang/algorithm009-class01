'''
方法一：暴力循环
超出时间限制

'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums[-1]
            for j in range(len(nums)):
                temp, nums[j] = nums[j], temp

'''
方法二： 直接定位元素旋转之后的位置

问题： 第一次没有考虑到k为偶数的情况，结果就是只能调换一半的元素。
       后增加一个while循环， 判断条件即为 元素位置回到起点。

'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        count = 0

        for i in range(n):
            move = i
            temp = nums[i]
            while True:
                move = (move+k)%n
                temp, nums[move] = nums[move], temp
                count += 1
                if move == i:
                    break
            if count >= n:
                break

'''
方法三： 反转数组
通过把整个数组 以及 前 K 个数组， 后 N-K 个数组分别反转，得到结果

'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums))
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))

    def reverse(self, nums, start, end):
        end -= 1
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
