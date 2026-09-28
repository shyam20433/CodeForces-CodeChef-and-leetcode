str1=str(input())
str2=str(input())
res=""
for i in range(len(str1)):
    if str1[i]!=str2[i]:
        res+='1'
    else:
        res+='0'
print(res)