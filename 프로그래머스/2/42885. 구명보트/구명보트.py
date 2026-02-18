def solution(people, limit):
    people.sort()  # 정렬 해야 투포인터가 의미가 있음.
    left = 0
    right = len(people) - 1
    answer = 0
    
    while left <= right:
        if people[left]+people[right] <= limit:
            left += 1
    
        right -= 1
        answer += 1
    return answer


## 해설
# 문제 풀이
    # 투포인터. 가장 가벼운 + 가장 무거운 을 비교하며 최적의 상태일 때 보트에 태워보내기