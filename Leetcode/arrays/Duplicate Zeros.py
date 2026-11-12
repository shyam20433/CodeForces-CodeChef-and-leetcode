class Solution:
    def duplicateZeros(self, nums: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero=nums.count(0)
        for i in range(len(nums)-1,-1,-1):
            value=nums[i]
            if i+zero<len(nums):
                nums[i+zero]=value
            if value==0:
                zero-=1
                if i+zero<len(nums):
                    nums[i+zero]=value


        # i=0
        # while i<len(nums)-1:
        #     curr=nums[i] #10230450
        #     if nums[i]==0:
        #         n=len(nums)-2
        #         while n>i:
        #             nums[n+1]=nums[n]
        #             n-=1
        #         nums[i+1]=0
        #         i+=1
        #     i+=1

        