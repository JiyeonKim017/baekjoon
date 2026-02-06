def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(cur_k, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(len(dungeons)):
            if not visited[i] and cur_k >= dungeons[i][0]:
                visited[i] = True
                dfs(cur_k - dungeons[i][1], count + 1)
                visited[i] = False

    dfs(k, 0)
    return answer