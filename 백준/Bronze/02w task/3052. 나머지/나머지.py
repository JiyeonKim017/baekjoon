remainders = set() # 중복을 제거해주는 마법의 바구니(집합) 생성

for _ in range(10):
    num = int(input())
    remainders.add(num % 42) # 리스트의 append 대신 set은 add를 써요!

# 중복이 제거된 바구니에 숫자가 몇 개 들어있는지 출력
print(len(remainders))

## 1. 10번 입력받으며 바로 % 42를 계산해서 리스트로 만듦
## 2. 그 리스트를 set()으로 감싸서 중복 제거
## 3. 그 길이를 len()으로 측정
# print(len(set(int(input()) % 42 for _ in range(10))))