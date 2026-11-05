t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if l > 0 or r < 0:
        print(r - l)
    elif l + r == 0:
        print(0)
    else:
        print(abs(l + r) - 1)