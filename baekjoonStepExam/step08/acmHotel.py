t = int(input())
roomNum = []
for i in range(0, t) :

    h, w, n = input().split()
    h = int(h)
    w = int(w)
    n = int(n)
            
    if  1 <= h and w <= 99 and 1 <= n and n <= h * w :
        if n % h == 0 :
            floor = h
            num = n // h
        else :
            floor = n % h
            num = (n // h) + 1
            
        roomNum.append(floor * 100 + num)
        
    else :
        exit

for i in roomNum :
    print(i, end='\n')