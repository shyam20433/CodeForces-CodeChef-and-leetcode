class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left=0
        right=len(s)-1
        s=list(s)
        while left<right:
            if s[left]!=s[right]:
                temp=min(s[left],s[right])
                s[left]=temp
                s[right]=temp

            left+=1
            right-=1
        return "".join(s)
        