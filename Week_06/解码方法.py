class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n==0: return 0
        dp = [1,0]
        dp[1] = 1 if s[0]!='0' else 0 
        for i in range(2,n + 1):
            dp.append(0)
            if s[i - 1]!='0':
                dp[i] = dp[i - 1]
            if s[i-2:i]>='10' and s[i-2:i]<='26':
                dp[i] += dp[i-2]
        
        return dp[-1]