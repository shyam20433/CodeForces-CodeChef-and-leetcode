t=int(input())
for _ in range(t):
    a,b=list(map(int,input().split()))
    if b>=a:
        print(-1)
    else:
        print(min(b,a-b))