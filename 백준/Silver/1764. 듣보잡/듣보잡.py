import sys

n, m = map(int, sys.stdin.readline().split())

unheard = set()
for _ in range(n):
    unheard.add(sys.stdin.readline().strip())

result = []
for _ in range(m):
    name = sys.stdin.readline().strip()
    if name in unheard:
        result.append(name)

result.sort()
print(len(result))
for name in result:
    print(name)