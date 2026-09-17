class Solution:
    def compress(self, s: list[str]) -> int:
        res=""
        count=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                if count>1:
                    res+=s[i]+str(count)
                else:
                    res+=s[i]
                count=1
        if count>1:
            res+=s[-1]+str(count)
        else:
            res+=s[-1]
        
        for i in range(len(res)):
            s[i]=res[i]
        return len(res)



        