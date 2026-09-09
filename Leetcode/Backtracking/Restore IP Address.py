class Solution:
    def restoreIpAddresses(self, word: str) -> List[str]:
        res=[]
        def backtrack(start,sol):
            if len(sol)==4 and start==len(word):
                res.append(".".join(sol))
                return
            
            for length in [1,2,3]:
                sub=word[start:start+length]
                if start+length>len(word):
                    break
                
                if int(sub)>255:
                    break
                if len(sub)>1 and sub[0]=="0":
                    break
                
                backtrack(start+length,sol+[sub])
        backtrack(0,[])
        return res
                
