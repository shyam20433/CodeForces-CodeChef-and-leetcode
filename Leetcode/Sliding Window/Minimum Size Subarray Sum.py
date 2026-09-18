class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        mini=float('inf')
        total=0
        left=0
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                mini=min(mini,i-left+1)
                total-=nums[left]
                left+=1
        return mini if mini!=float('inf') else 0

        