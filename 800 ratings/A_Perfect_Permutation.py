n=int(input())
if n%2==1:
    print(-1)
else:
    nums=[*range(1,n+1)]
    nums[0::2],nums[1::2]=nums[1::2],nums[0::2]
    print(*nums)