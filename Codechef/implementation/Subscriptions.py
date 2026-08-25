import math
t=int(input())
for _ in range(t):
    n,num=list(map(int,input().split()))
    sub=math.ceil(n/6)
    print(sub*num)