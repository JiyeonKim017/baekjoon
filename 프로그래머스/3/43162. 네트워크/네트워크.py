def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(now):
        visited[now] = True
        for neighbor in range(n):
            if computers[now][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer