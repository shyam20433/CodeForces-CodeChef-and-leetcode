class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res=[]
        for i in operations:
            if i=="D" and res:
                res.append(res[-1]*2)
            elif i=="+" and len(res)>1:
                res.append(res[-1]+res[-2])
            elif i=="C" and res:
                res.pop()
            else:
                res.append(int(i))
        return sum(res)