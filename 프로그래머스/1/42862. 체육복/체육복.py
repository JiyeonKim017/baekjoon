def solution(n, lost, reserve):
    new_lost = sorted(list(set(lost) - set(reserve)))
    new_reserve = sorted(list(set(reserve) - set(lost)))
    
    for r in new_reserve:
        if r-1 in new_lost:
            new_lost.remove(r-1)
        elif r+1 in new_lost:
            new_lost.remove(r+1)
            
    return n - len(new_lost)


## 해설
# 1. 잃어버렸는데 여분 있으면 자기꺼 입음 -> 옷 있는 애가 된거임.
# 2. lost, reserve 에서 1. 빼낸 뒤에 reserver 를 돌면서 lost에 빌려줄만한 애가 있나 확인하고 앞번호 > 뒷번호 순으로 돌면서 빌려줌 !
# 3. 최종적으로 lost는 걍 체육복 없는 애들임. 전체 - lost하면 체육 듣는 애 나옴