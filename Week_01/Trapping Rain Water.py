class Solution:
    def trap(self, height: List[int]) -> int:

        s1, s2 = 0, 0
        max1, max2 = 0, 0

        for i in range(len(height)):
            if height[i] > max1:
                max1= height[i]
            s1 += max1

            if height[len(height) - 1 - i] > max2:
                max2 = height[len(height) - 1 - i]
            s2 += max2
        return s1 + s2 - max1 * len(height) - sum(height)