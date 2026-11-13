t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    count=0
    for i in range(0,n,k+1):
        count+=nums[i]
    if count%2:
        print("Alice")
    else:
        print("Bob")