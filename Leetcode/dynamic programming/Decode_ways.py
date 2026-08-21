class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0]=="0":
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,len(s)+1):
            one=int(s[i-1])
            two=int(s[i-2]+s[i-1])

            if one!=0:
                dp[i]+=dp[i-1]
            if 10<=two<=26:
                dp[i]+=dp[i-2]
        return dp[len(s)]
        