    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for l in range(i + 1):
                r = i - l
                temp = s[l:len(s) - r]
                if temp == temp[::-1]:
                    return temp
        return ''