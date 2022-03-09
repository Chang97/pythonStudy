a, b, v = input().split()
a = int(a)
b = int(b)
v = int(v)
h = 0
cnt = 0

if 1 <= b and b < a and a <= v and b <= 1000000000 :
    while h < v :
        h += a
        cnt += 1
        if h >= v :
            break
        else :
            h -= b
    print(cnt)
else :
    exit()
