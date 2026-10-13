class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        hash=defaultdict(int)
        for i in nums:
            hash[i]+=1
        dup=-1
        missing=-1
        for i in range(1,1+len(nums)):
            if hash[i]==2:
                dup=i
            if hash[i]==0:
                missing=i
        return [dup,missing]