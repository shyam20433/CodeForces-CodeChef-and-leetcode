t=int(input())
for _ in range(t):
    n=int(input())
    s=str(input())
    isSorted=True
    for i in range(n-1):
        if s[i]=="1" and s[i+1]=="0":
            isSorted=False
            break
    if isSorted:
        print(0)
        continue
    if s[0]=="1":
        print(s.count("0"))
        continue
    total_zero=s.count("1")
    minimum=total_zero
    first_one=s.find("1")
    ones_in_left_side=0
    total_zero=s.count("0")
    zero_in_right=total_zero

    for i in range(n):
        if s[i]=="0":
            zero_in_right-=1
        if i>=first_one:
            current_count=zero_in_right+ones_in_left_side
            if current_count<minimum:
                minimum=current_count

        if s[i]=="1":
            ones_in_left_side+=1
    print(minimum)