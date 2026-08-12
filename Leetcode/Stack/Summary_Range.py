class Solution:
    def summaryRanges(self, nums):
        result=[]
        res=[]
        for i in range(len(nums)):
            if not res:
                res.append(nums[i])
            elif nums[i]==res[-1]+1:
                res.append(nums[i])
            else:
                if len(res)>1:
                    result.append(str(res[0])+"->"+str(res[-1]))
                else:
                    result.append(str(res[0]))
                res=[nums[i]]
        if res:
            if len(res)>1:
                result.append(str(res[0])+"->"+str(res[-1]))
            else:
                result.append(str(res[0]))
                
            print(res)
        return result
                

        