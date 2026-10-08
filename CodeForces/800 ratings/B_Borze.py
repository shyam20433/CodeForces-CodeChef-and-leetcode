word=str(input())
ans=""
res=""
for i in word:
    res+=i
    # print(res)
    if res==".":
        ans+="0"
        res=""
    elif res=="-.":
        ans+="1"
        res=""
    elif res=="--":
        ans+="2"
        res=""
    else:
        continue
print(ans)

