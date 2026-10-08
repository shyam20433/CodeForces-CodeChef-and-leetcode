# https://codeforces.com/problemset/problem/49/A
# link 

words=str(input())
words="".join(words.split())
if words[-2] in "AEIOUYaeiouy":
    print("YES")
else:
    print("NO")