class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        maxi=float('inf')
        for length in range(l,r+1):
            for i in range(len(nums)-length+1):
                sub=sum(nums[i:i+length])
                if 0<sub<maxi:
                    maxi=sub
        return maxi if maxi!=float('inf') else -1