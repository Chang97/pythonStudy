N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]
pt = 0
ans = []
print(arr)
for _ in range(N) :
    pt += K - 1
    pt %= len(arr)
    ans.append(arr.pop(pt))

print(f"<{', '.join(map(str,ans))}>")

# [1, 2, 3, 4, 5, 6, 7]
