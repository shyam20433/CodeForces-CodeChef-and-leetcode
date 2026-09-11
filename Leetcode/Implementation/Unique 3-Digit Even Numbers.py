class Solution:
    def totalNumbers(self, nums: List[int]) -> int:
        seen=set()
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            for j in range(len(nums)):
                if i==j:
                    continue
                for k in range(len(nums)):
                    if i==k or j==k:continue
                    if nums[k]%2==0:
                        num=nums[i]*100+nums[j]*10+nums[k]
                        seen.add(num)
        return len(seen)