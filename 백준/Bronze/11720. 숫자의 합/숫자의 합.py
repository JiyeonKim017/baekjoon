n = int(input())
li = list(map(int, input()))
total = 0
for i in range(n):
    total = sum(x for x in li)
print(total)