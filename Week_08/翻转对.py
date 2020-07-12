class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, left, right):
            if left >= right:
                return 0
            mid = left + (right - left) // 2
            i = tmp = left
            j = mid + 1
            cnt = merge(nums, left, mid) + merge(nums, mid + 1, right)
            result = []
            while j <= right:
                while tmp <= mid and nums[tmp] / 2.0 <= nums[j]:
                    tmp += 1
                while i <= mid and nums[i] < nums[j]:
                    result.append(nums[i])
                    i += 1
                result.append(nums[j])
                j += 1
                cnt += mid - tmp + 1
            result += nums[i:mid + 1]
            nums[left:right+1] = result[:]
            return cnt
        if not nums:
            return 0
        return merge(nums, 0, len(nums) - 1)