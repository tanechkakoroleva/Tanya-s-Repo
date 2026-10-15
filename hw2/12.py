n = int(input())
if 11<= n%100 <=14:
    print(n, "попугаев")
else:
    a = n % 10
    if a==1:
        print(n, "попугай")
    elif 2<=a<=4:
        print(n, "попугая")
    else:
        print(n, "попугаев")
