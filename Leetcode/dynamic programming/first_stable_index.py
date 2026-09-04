class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        left=[0]*len(nums)
        right=[0]*(len(nums))
        left[0]=nums[0]
        right[-1]=nums[-1]
        for i in range(1,len(nums)):
            left[i]=max(left[i-1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            right[i]=min(right[i+1],nums[i])
        
        for i in range(len(nums)):
            if left[i]-right[i]<=k:
                return i
        return -1
        
            
        