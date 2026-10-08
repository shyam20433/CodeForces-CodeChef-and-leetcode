import math
n=int(input())
if n<0:
    print("NO")
else:
    squared=(8*n)+1
    root=math.isqrt(squared)
    if root*root==squared:
        print("YES")
    else:
        print("NO")