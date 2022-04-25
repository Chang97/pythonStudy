max = 0
num = int(input())

if num < 3 or num > 5000 :
    exit()

while num >= 0 :
    if num % 5 == 0 :
        max += num // 5
        print(max)
        break
    num -= 3
    max += 1
else :
    print(-1)