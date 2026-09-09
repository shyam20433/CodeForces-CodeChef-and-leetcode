from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        res=[]
        while n:
            res.append(n%10)
            n//=10
        hash=Counter(res)
        total=0
        for k,v in hash.items():
            total+=k*v
        return total