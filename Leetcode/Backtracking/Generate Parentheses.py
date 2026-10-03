class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def back(open,close,s):
            if open==close and open+close==n+n:
                res.append(s)
                return
            
            if open<n:
                back(open+1,close,s+"(")
            if close<open:
                back(open,close+1,s+")")
        
        back(0,0,"")
        return res