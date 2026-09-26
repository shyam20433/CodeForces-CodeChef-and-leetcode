class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<=1:return 0
        count=0
        left=0
        p=1
        for right in range(len(nums)):
            p*=nums[right]

            while p>=k:
                p/=nums[left]
                left+=1
            
            count+=right-left+1
        return count
        