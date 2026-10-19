class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        digit_sum=lambda x: sum(map(int,str(x)))
        rank={x:k for k,x in enumerate(sorted(nums,key=lambda x: (digit_sum(x),x)))}
        print(rank)
        home=[rank[x] for x in nums]
        print(home)
        swap=0
        for i in range(len(home)):
            while home[i]!=i:
                j=home[i]
                home[i],home[j]=home[j],home[i]
                swap+=1
        return swap