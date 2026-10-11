class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total=0
        for i in range(len(nums)):
            if len(nums)%(i+1)==0:
                total+=nums[i]*nums[i]
        return total