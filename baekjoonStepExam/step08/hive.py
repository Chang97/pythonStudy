num = int(input())
room = 1
befRoom = 1
loopCnt = 1
cnt = 0

if num <= 0 and num >= 1000000000 :
    exit()

if num == 1 :
    print(1)
    exit()


while True :
    room += 6 * loopCnt
    if loopCnt - 1 != 0 :
        befRoom += 6 * (loopCnt -1)
    if num > befRoom and num <= room :
        cnt = loopCnt + 1
        break
    loopCnt += 1

print(cnt)
