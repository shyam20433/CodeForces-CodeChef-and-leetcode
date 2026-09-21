t=int(input())
for _ in range(t):
    a,b,c=list(map(int,input().split()))
    print(max(abs(a-b),abs(a+c-(b))))
    