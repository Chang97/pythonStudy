t = int(input())
roomNum = []
for i in range(0, t) :

    h, w, n = input().split()
    h = int(h)
    w = int(w)
    n = int(n)
            
    if  1 <= h and 1 <= w and h <= 99 and w <= 99 and 1 <= n and n <= h * w :
        floor = n % h
        num = (n // h) + 1
        
        if num // 10 == 0 :
            roomNum.append(str(floor) + "0" + str(num))
        else :
            roomNum.append(str(floor) + str(num))
        
    else :
        exit

for i in roomNum :
    print(i, end=' ')