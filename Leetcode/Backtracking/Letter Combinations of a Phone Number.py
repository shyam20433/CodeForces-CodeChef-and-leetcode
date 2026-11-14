class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters= { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res=[]
        sol=[]
        
        def backtrack(i):
            if len(sol)==len(digits):
                res.append("".join(sol))
                return
            
            char=digits[i]
            for c in letters[char]:
                sol.append(c)
                backtrack(i+1)
                sol.pop()
        backtrack(0)
        return res