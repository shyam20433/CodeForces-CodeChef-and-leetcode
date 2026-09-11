n=int(input())
nums=list(map(int,input().split()))
res=[]
for i in range(1,n+1):
    res.append(nums.index(i)+1)
print(*res)