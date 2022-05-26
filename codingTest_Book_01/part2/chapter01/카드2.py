from collections import deque

# deque 에서 메서드는 오른쪽 기준 왼쪽은 left붙음.
dq = deque()
for i in range(1, int(input()) + 1) :
    dq.append(i)

while len(dq) > 1 :
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())


