class Solution:
    def bubbleSort(self,nums):
        # code here
        for i in range(len(nums)):
            isSwapped=False
            for j in range(len(nums)-i-1):
                if nums[j+1]<nums[j]:
                    nums[j+1],nums[j]=nums[j],nums[j+1]
                    isSwapped=True
            if not isSwapped:
                break
        return nums