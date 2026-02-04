li = list(map(int, input().split()))
total = 0
for i in range(5):
    total = sum(x**2 for x in li)
print(total%10)