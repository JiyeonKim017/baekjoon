def solution(tickets):
    tickets.sort()
    used = [False] * len(tickets)
    
    def dfs(now, path):
        if len(path) == len(tickets) + 1:
            return path
        
        for i in range(len(tickets)):
            if not used[i] and tickets[i][0] == now:
                used[i] = True
                result = dfs(tickets[i][1], path + [tickets[i][1]])
                if result:
                    return result
                used[i] = False
        return None
        
    return dfs("ICN", ["ICN"])