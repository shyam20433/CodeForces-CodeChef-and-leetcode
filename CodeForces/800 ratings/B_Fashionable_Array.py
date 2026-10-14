t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))

    cmt=[0]*(101)
    for i in nums:
        cmt[i]+=1
    res=[]
    for i in range(1,n+1):
        for j in range(100,0,-1):
            if cmt[j]>=i:
                res.append(j)
    print(*res)