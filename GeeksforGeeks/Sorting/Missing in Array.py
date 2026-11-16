class Solution:
    def missingNum(self, nums: list[int]) -> int:
        i=0
        while i<len(nums):
            curr=nums[i]-1
            if 0<=curr<len(nums) and nums[i]!=nums[curr]:
                nums[i],nums[curr]=nums[curr],nums[i]
            else:
                i+=1
        
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1
        return len(nums)+1
        # code here