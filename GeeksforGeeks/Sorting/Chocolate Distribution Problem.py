class Solution:
    def findMinDiff(self, arr, m):
        # code here
        def sort(nums):
            if len(nums)<=1:
                return nums
            pivot=nums[0]
            left=[i for i in nums[1:] if i<=pivot]
            right=[i for i in nums[1:] if i>pivot]
            return sort(left)+[pivot]+sort(right)
        arr=sort(arr)
        #print(arr)
        sub=arr[:m]
        mini=sub[-1]-sub[0]
        for i in range(m,len(arr)):
            sub.append(arr[i])
            sub.pop(0)
            mini=min(mini,sub[-1]-sub[0])
        return mini