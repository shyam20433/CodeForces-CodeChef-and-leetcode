class Solution:
    def longestMonotonicSubarray(self, nums: any) -> int:
        inc=1
        dec=1
        maxi=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc+=1
                dec=1
            elif nums[i]<nums[i-1]:
                dec+=1
                inc=1
            else:
                inc=1
                dec=1
            maxi=max(maxi,inc,dec)
        return maxi