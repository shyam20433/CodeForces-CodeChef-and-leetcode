n=int(input())
for i in range(n):
    num=int(input())
    num=num+1
    isPrime=True
    for j in range(2,num):
        if num%j==0:
            isPrime=False
    if isPrime:
        print("YES")
    else:
        print("NO")