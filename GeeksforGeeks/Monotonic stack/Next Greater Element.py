class Solution:
    def nextLargerElement(self, nums):
        # code here
        res=[-1]*(len(nums))
        stack=[]
        for i in range(len(nums)):
            curr=nums[i]
            while stack and curr>nums[stack[-1]]:
                res[stack.pop()]=curr
            stack.append(i)
        return res