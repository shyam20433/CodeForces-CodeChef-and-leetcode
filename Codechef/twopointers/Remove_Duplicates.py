n=int(input())
for _ in range(n):
    m=int(input())
    nums=list(map(int,input().split()))
    j=0
    for i in range(m):
        if nums[i]!=nums[j]:
            j+=1
            nums[i],nums[j]=nums[j],nums[i]
    print(j+1)
    print(*nums[:j+1])
