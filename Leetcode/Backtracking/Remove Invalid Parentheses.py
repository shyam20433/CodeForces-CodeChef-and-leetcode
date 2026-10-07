class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        # this is straigth and gives only one valid string
        # res=[]
        # def backtrack(start,balance,sub):
        #     if start==len(s) and balance==0:
        #         res.append("".join(sub))
        #         return 
        #     if start>len(s)-1:
        #         return
        #     sub.append(s[start])
        #     if s[start]=="(":
        #         balance+=1
        #         print("balanace when ( ", balance , sub)
        #     elif s[start]==")":
        #         balance-=1
        #         print("balanace when ) ", balance , sub)
        #     if balance<0:
        #         if sub and sub[-1]==")":
        #             sub.pop()
        #             balance=0
        #             print("balanace rest ",balance,sub)
        #     return backtrack(start+1,balance,sub)
        # backtrack(0,0,[])
        # return res if res else [""]


        #according to the hint take a char or leave the char
        #count invalid paran
        open=0
        close=0
        for i in s:
            if i=="(":
                open+=1
            elif i==")":
                if open>0:
                    open-=1
                else:
                    close+=1
        print(open,close)
        res=[]
        def backtrack(start,open,close,balance,sol):
            #stoping condition 
            if start==len(s) and open==0 and close==0 and balance==0:
                sub="".join(sol)
                if sub not in res:
                    res.append(sub)
                return 
            #boundary check 
            if balance<0:
                return # invalid para
            if start>len(s)-1:
                return
            #skip the character 
            char=s[start]
            if char=="(" and open>0:
                backtrack(start+1,open-1,close,balance,sol)
            elif char==")" and close>0:
                backtrack(start+1,open,close-1,balance,sol)
            
            sol.append(char)
            #take the character
            if char=="(":
                backtrack(start+1,open,close,balance+1,sol)
            elif char==")":
                backtrack(start+1,open,close,balance-1,sol)
            else:
                backtrack(start+1,open,close,balance,sol)
            sol.pop()
        backtrack(0,open,close,0,[])
        return res


            
        