import math
n=int(input())
square=math.sqrt((8*n)+1)
if isinstance(square,float):
    print("NO")
elif isinstance(square,Decimal):
    print("YES")