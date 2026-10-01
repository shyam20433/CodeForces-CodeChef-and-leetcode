class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res=[]
        count=0
        for i in seq:
            if i=="(":
                count+=1
                res.append(count%2)
            else:
                res.append(count%2)
                count-=1
        return res
        