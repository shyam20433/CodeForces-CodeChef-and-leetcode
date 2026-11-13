t=int(input())
for _ in range(t):
    n=int(input())
    nums=sorted(list(map(int,input().split())))
    res=[nums[0]]
    if n>1:
        for i in range(2,n):
            res.append(nums[i])
        res.append(nums[1])
        print(n-2+1)
        print(*res)
    else:
        print(1)
        print(*res)
