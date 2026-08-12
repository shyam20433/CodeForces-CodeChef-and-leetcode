# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    mini=n
    left=0
    maxi=0
    for right in range(len(nums)):
        if right>0 and nums[right]-nums[right-1]>2:
            left=right
        if right+1==n or nums[right+1]-nums[right]>2:
            curr=right-left+1
            mini=min(mini,curr)
            maxi=max(maxi,curr)
    print(*[mini,maxi])

            