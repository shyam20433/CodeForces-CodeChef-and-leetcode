from collections import Counter
word1=str(input())
word2=str(input())
word=str(input())
hash=Counter(word)
isFyn=True
i=0
while i<len(word1):
    if hash[word1[i]]==0:
        isFyn=False
        break
    hash[word1[i]]-=1
    i+=1
i=0
while i<len(word2):
    if hash[word2[i]]==0:
        isFyn=False
        break
    hash[word2[i]]-=1
    i+=1

if not isFyn:
    print("NO")
else:
    for k,v in hash.items():
        if v>0:
            isFyn=False
            break
    if isFyn:
        print("YES")
    else:
        print("NO")
 