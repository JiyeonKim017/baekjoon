n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
hap = 0
for i in range(n):
    hap += scores[i]/m*100
print(hap/n)