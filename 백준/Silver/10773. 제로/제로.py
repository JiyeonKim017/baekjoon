import sys
input = sys.stdin.readline

k = int(input())
stack = []

for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
        
print(sum(stack))


## 해설
# k : 입력값 개수
# input : sys 로 가져오기 위한 줄임말
# num : 입력값들
# num을 stack에 쌓거나 0이면 빼서 최종 stack 의 sum 출력