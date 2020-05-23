class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = [str(x) for x in digits]
        return list(map(int, str(int(''.join(temp)) + 1)))