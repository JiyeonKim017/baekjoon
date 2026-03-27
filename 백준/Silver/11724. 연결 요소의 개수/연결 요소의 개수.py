import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (N + 1)
    count = 0
    
    for node in range(1, N + 1):
        if not visited[node]:
            count += 1
            queue = deque([node])
            visited[node] = True
            while queue:
                cur = queue.popleft()
                for nb in graph[cur]:
                    if not visited[nb]:
                        visited[nb] = True
                        queue.append(nb)
    
    print(count)

solution()