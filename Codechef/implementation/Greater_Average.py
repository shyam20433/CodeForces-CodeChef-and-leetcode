n=int(input())
for _ in range(n):
    ans="NO"
    a,b,c=list(map(int,input().split()))
    average=(a+b)/2
    if average>c:
        ans="YES"
    print(ans)
