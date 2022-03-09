max = 0
num = int(input())

if num < 3 or num > 5000 :
    exit()

if num % 5 == 0 :
    max = num // 5
elif (num - 5) % 3 == 0 :
    max = 1 + (num - 5) // 3
elif (num % 5) % 3 == 0 :
    max = num // 5
    max += (num % 5) // 3
elif num % 3 == 0 :
    max = num // 3
else :
    max = -1

print(max)
