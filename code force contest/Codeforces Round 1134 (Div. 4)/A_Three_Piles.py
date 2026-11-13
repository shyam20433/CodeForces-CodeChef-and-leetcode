t=int(input())
for _ in range(t):
    nums=sorted(list(map(int,input().split())))
    nums[0]+=1
    nums[-1]-=1
    if nums[0]==nums[1]==nums[-1]:
        print("YES")
    else:
        print("NO")
    