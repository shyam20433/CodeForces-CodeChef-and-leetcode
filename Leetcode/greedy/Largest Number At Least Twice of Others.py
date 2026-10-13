class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        maxi=max(nums)
        pos=-1
        for i in range(len(nums)):
            if nums[i]*2>maxi and nums[i]!=maxi:
                return -1
            if nums[i]==maxi:
                pos =i
        return pos