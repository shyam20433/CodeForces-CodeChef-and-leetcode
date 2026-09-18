class Solution:
    def numOfSubarrays(self, nums: list[int], k: int, threshold: int) -> int:
        count=0
        total=0
        for i in range(k):
            total+=nums[i]
        if total/k>=threshold:
            count+=1
        
        for i in range(k,len(nums)):
            total+=nums[i]-nums[i-k]
            if total/k>=threshold:
                count+=1
        return count