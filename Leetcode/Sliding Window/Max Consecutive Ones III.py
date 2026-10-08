class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left=0
        zero=0
        maxi=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
            while zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi