import sys
n = int(input())
grid = [ list(map(int, input())) for _ in range(n) ]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []

def dfs(x, y):
	grid[x][y] = 0
	count = 1
	
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		
		if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
			count += dfs(nx, ny)
			
	return count

for i in range(n):
	for j in range(n):
		if grid[i][j] == 1:
			result.append(dfs(i, j))

result.sort()

print(len(result))
for count in result:
	print(count)