t = int(input())
valArr = []

for i in range(t) :
    k = int(input()) + 1
    n = int(input())
    if k < 1 and n > 14 :
        exit()
    arr = [[0 for i in range(n)] for j in range(k)]
    
    for j in range(n) :
        arr[0][j] = j + 1
    for floor in (1, k - 1) :
        for num in range(n) :
            if num == 0 :
                arr[floor][num] = 1
            else :
                arr[floor][num] = arr[floor -1][num] + arr[floor][num - 1]
    valArr.append(arr[k -1][n - 1])

for val in valArr :
    print(val)

    