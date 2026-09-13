class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def helper(mid):
            count=1
            total=0
            for i in nums:
                total+=i
                if total>mid:
                    count+=1
                    total=i
            return count<=k
        left=max(nums)
        right=sum(nums)
        while left<right:
            mid=left+(right-left)//2
            if helper(mid):
                right=mid
            else:
                left=mid+1
        return left