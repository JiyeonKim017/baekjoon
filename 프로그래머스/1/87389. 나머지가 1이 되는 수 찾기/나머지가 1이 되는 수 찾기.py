# 말로 설명 - n이 x로 나눴을 때, 나머지가 1이 되는 가장 작은 자연수 x
def solution(n):
    answer = 0
    for x in range(2, n):
        if n%x==1:
            answer = x
            break
    return answer