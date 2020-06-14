class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        dp5, dp10 = 0, 0

        for bill in bills:
            if bill == 5:
                dp5 += 1
            elif bill == 10:
                dp5 -= 1
                dp10 += 1
            else:
                if dp10 > 0:
                    dp10 -= 1
                    dp5 -= 1
                else:
                    dp5 -= 3
            if dp5 < 0 or dp10 < 0:
                return False
        return True