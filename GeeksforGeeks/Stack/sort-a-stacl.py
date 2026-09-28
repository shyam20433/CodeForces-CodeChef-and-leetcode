class Solution:
    def sortStack(self, nums):
        # code here
        for i in range(len(nums)-1):
          small=i
          for j in range(i+1,len(nums)):
            if nums[j]<nums[small]:
              nums[j],nums[small]=nums[small],nums[j]
        return nums