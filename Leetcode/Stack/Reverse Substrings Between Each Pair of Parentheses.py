class Solution:
    def reverseParentheses(self, s: str) -> str:
        #but this is not optimal approach 
        stack=[]
        res=[]
        for i,c in enumerate(s):
            res.append(c)
            if c=="(":
                stack.append(i)
            if c==")":
                index=stack.pop()
                res[index:i+1]=reversed(res[index:i+1])
            
        res[:]=[i for i in res if i not in '()']
        return "".join(res)



        
        
        
        