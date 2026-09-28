class Solution:
    def preToInfix(self, s):
        stack=[]
        # Code here
        operators="+-()*%/"
        
        for i in range(len(s)-1,-1,-1):
            if s[i] not in operators:
                stack.append(str(s[i]))
            else:
                
                last=stack.pop()
                last_before=stack.pop()
                stack.append(("("+last+s[i]+last_before+")"))
        return stack.pop()