class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        count=0
        for i in s:
            if i=="(":
                if count>0:
                    res+=i
                count+=1
            elif i==")":
                count-=1
                if count>0:
                    res+=i
                
        return res