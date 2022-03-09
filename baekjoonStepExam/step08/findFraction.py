diagonal = 1
lNum = 0
rNum = 0
cnt = 1

input = int(input())

if input < 0 and input > 10000000 :
    exit()

while diagonal <= input :
    if diagonal + cnt > input :
        break

    diagonal += cnt
    cnt += 1

if cnt % 2 == 0 :
    rNum = cnt - (input - diagonal)
    lNum = cnt - rNum + 1
else :
    lNum = cnt - (input - diagonal)
    rNum = cnt - lNum + 1

print(str(lNum) + "/" + str(rNum))

