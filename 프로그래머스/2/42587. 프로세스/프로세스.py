from collections import deque

def solution(priorities, location):
    # (중요도, 인덱스) 튜플로 큐 생성
    queue = deque( [p,i] for i, p in enumerate(priorities))
    answer = 0
    
    while queue:
        current = queue.popleft()
        
        if any(current[0] < p[0] for p in queue):
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer