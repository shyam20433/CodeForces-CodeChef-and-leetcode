class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        # for i in range(len(arr)-1):
        #     small=i
        #     for j in range(i+1,len(arr)):
        #         if arr[j]<arr[small]:
        #             small=j
        #     arr[i],arr[small]=arr[small],arr[i]
        # this is o(n^2) so TLE we go for o(nlogn) => merge or quick sort 
        
        #this is quick sort
        def sort(nums):
            if len(nums)<=1:
                return nums
            pivot=nums[0]
            left=[i for i in nums[1:] if i<=pivot]
            right=[i for i in nums[1:] if i>pivot]
            return sort(left)+[pivot]+sort(right)
        arr=sort(arr)
        return arr[k-1]
