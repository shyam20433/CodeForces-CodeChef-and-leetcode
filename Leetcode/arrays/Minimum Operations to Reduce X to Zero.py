class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x # this is middle sum of the array ...we just find the highest len of the mid array sum and remove the total length !! 
        if target<0:
            return -1
        if target==0:
            return len(nums)
        if min(nums)>x:
            return -1
        
        maxi=-1
        total=0
        left=0
        for right in range(len(nums)):
            total+=nums[right]
            while total>target:
                total-=nums[left]
                left+=1
            if total==target:
                maxi=max(maxi,right-left+1)
        
        return len(nums)-maxi if maxi!=-1 else -1