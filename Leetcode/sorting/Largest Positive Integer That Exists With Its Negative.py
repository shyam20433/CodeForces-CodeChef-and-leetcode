import heapq
class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        res=[]
        heapq.heapify(res)
        for i in range(len(nums)):
            heapq.heappush(res,nums[i])
        while res:
            num=heapq.heappop(res)
            if -num in res:
                return -num
        return -1