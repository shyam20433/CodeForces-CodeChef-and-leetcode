n,k=list(map(int,input().split()))
odd=(n+1)//2
if odd>=k:
    print(2*k-1)
else:
    print(2*(k-odd))