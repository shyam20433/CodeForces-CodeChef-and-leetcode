class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            digitSum=0
            while num:
                digitSum+=num%10
                num//=10
            if digitSum==i:
                return i
        return -1
        