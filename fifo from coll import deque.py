from collections import deque

l=deque([])

l.append(10)
print(list(l))

l.append(20)
print(list(l))

l.append(30)
print(list(l))

l.popleft()
print(list(l))

l.popleft()
print(list(l))
