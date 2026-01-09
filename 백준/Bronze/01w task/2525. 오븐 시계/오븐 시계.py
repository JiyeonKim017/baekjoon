h, m = map(int, input().split())
p = int(input())

a = (((h*60)+m+p)//60)%24
b = ((h*60)+m+p)%60

print(a, b)