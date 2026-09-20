class Solution:
    def leaders(self, nums):
        # code here
        res=[]
        maxi=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>=maxi:
                maxi=nums[i]
                res.append(nums[i])
        return res[::-1]
            