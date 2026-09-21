class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        res=[-1]*(len(nums))
        stack=[]
        for j in range(len(nums)*2):
            i=j%len(nums)
            curr=nums[i]
            while stack and curr>nums[stack[-1]]:
                res[stack.pop()]=curr
            
            if j<len(nums):
                stack.append(i)
        return res