class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dp = [0]*(n+1)
        for c1 in text1:
            pre = 0
            for i in range(1,n+1):
                temp = dp[j]
                if text2[i-1] == c1:
                    dp[j] = pre+1
                else:
                    dp[j] = max(dp[j],dp[j-1])
                pre = temp
        return dp[-1]