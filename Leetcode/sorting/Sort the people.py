import heapq
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        # hash={a:b for a,b in zip(names,heights)}
        # hash=dict(sorted(hash.items(),key=lambda x:x[1],reverse=True))
        # return list(hash.keys())
        res=[]
        heapq.heapify(res)
        for i in range(len(names)):
            heapq.heappush(res,(-heights[i],names[i]))
        ans=[]
        while res:
            height,name=heapq.heappop(res)
            ans.append(name)
        return ans