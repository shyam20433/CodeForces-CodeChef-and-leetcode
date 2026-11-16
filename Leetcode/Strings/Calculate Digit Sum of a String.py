class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            res=[]
            for i in range(0,len(s),k):
                res.append(str(s[i:i+k]))
            s=""
            for num in res:
                total=0
                for i in num:
                    total+=int(i)
                s+=str(total)
        return str(s)