class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        #solve count prime before this 
        if s<=1:
            return []
        prime=[True]*(n+1)
        prime[0]=prime[1]=False
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n+1,i): # if n is a prime change n=> n+1
                    prime[j]=False
        res=[i for i,isPrime in enumerate(prime) if isPrime]
        # count=0
        # left=0
        # index=0
        # for right in range(len(res)):
        #     index=right
        #     count+=res[right]
        #     while count>s and left<=right:
        #         count-=res[left]
        #         left+=1
        #     if count==s:
        #         return res[left:right+1]
            
        # sub=res[left:index+1]
        # left=0
        # while sub:
        #     while count>s:
        #         count-=sub[left]
        #     if count<s:
        #         return res[left:index+1]
        # return []
        sol=[]
        count=0
        for num in res:
            if count+num<=s:
                sol.append(num)
                count+=num
            else:
                break
        return sol
            
        
            