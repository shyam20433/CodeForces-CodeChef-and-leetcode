class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        mini=float('inf')
        for i in range(1,len(nums),2):
            new=str(nums[i-1])+str(nums[i])
            mini=min(mini,int(new))
        return mini