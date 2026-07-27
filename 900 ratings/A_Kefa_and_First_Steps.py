n=int(input())
nums=list(map(int,input().split()))
if n==0:
    print(0)
else:
    count=1
    maxi=1
    for i in range(1,n):
        if nums[i-1]<=nums[i]:
            count+=1
        else:
            count=1
        if count>maxi:
            maxi=count
    print(maxi)
