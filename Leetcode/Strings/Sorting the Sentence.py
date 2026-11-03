class Solution:
    def sortSentence(self, s: str) -> str:
        hash=[[word[:-1],int(word[-1])] for word in s.split()]
        hash=list(sorted(hash,key=lambda x:x[-1]))
        print(hash)
        res=""
        for k,v in hash:
            res+=k
            res+=" "
        return res.strip()