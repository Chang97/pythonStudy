t = input()
t = int(t)
valArr = []
for i in range(0, t) :
    k, n = input().split()
    k = int(k) + 1
    n = int(n)

    if k >= 1 and n <= 14 :
        arr = []
        arr.append([])

        for j in range(0, n) :
            arr[0][n] = n
        
        for floor in range(1, k) :
            arr[floor].append([])
            for num in range(0, n) :
                if num == 0 :
                    arr[floor][num]= 1
                else :
                    arr[floor][num] = arr[floor - 1][num] + arr[floor][num - 1]
        
    valArr[i] = arr[k - 1][n - 1] 

for i in range(0, t) :
    print(valArr[i])



