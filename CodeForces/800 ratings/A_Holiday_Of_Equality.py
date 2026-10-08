n=int(input())
nums=list(map(int,input().split()))
maxi=max(nums)
ans=0
for i in range(n):
    ans+=(maxi-nums[i])
print(ans)
