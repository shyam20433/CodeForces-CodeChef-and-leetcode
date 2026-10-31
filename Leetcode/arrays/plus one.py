class Solution:
    def plusOne(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+1!=10:
                nums[i]+=1
                return nums
            nums[i]=0
        return [1]+nums