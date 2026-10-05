class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        depth=0
        for i in range(len(s)):
            if s[i]=="(": #=> "(" +=1 ")" -=1
                depth+=1
            else:
                depth-=1
                if s[i-1]=="(":#()=> depth=1  (()) => depth=2*(1) ((()))=> 2*(2*(2*(1))) so basically 2^depth
                    score+=2**depth # or 1<<depth (bit manipulation)
        return score