class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=[i for i in str(n)]
        i=len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        #123 i=2 j=3
        if i<0:
            return -1
        j=len(nums)-1
        while nums[i]>=nums[j]:
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=reversed(nums[i+1:])
        n="".join(nums)
        return int(n) if int(n)<=2**31-1 else -1