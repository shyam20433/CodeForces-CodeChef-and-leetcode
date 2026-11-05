class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        maxi=float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if abs(total-target)<abs(maxi-target):
                    maxi=total
                elif total<target:
                    left+=1
                else:
                    right-=1
        return maxi