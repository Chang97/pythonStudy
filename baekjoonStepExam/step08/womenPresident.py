t = int(input())
valArr = []
for _ in range(t) :
    
    k = int(input())
    n = int(input())
    if k >= 1 and k <= 14 and n >= 1 and n <= 14 :
        arr = [x for x in range(1, n + 1)]

        for i in range(k) :
            for j in range(1, n) :
                arr[j] += arr[j - 1]
        
        valArr.append(arr[-1])
    else :
        exit()

for i in valArr :
    print(i)
    