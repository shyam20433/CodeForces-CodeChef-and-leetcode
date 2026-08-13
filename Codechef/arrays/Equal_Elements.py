# cook your dish here
from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    hash=Counter(nums)
    print(n-max(hash.values()))