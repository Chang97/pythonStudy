books = dict()

for _ in range(int(input())) :
    name = input()
    
    if name in books:
        books[name] += 1
    else :
        books[name] = 1
maxVal = max(books.values())
arr = []
for k, v in books.items() :
    if v == maxVal :
        arr.append(k)

arr.sort()
print(arr[0])