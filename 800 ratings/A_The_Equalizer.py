n=int(input())
for _ in range(n):
    n,k=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    if sum(nums)%2==1:
        print("YES")
    else:
        if (n*k)%2==0:
            print("YES")
        else:
            print("NO")