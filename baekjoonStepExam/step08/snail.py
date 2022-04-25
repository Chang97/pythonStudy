a, b, v = input().split()
a = int(a)
b = int(b)
v = int(v)
h = 0

if 1 <= b and b < a and a <= v and v <= 1000000000 :
    h = (v - b) / (a - b)
    print(int(h) if h == int(h) else int(h) + 1)
else :
    exit()
