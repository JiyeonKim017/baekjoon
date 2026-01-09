remainders = set()

for _ in range(10):
    num = int(input())
    remainders.add(num % 42)

print(len(remainders))

ㅡㅡㅡ

1. 중복을 제거해주는 집합 (set) 으로 문제 해결
2. set엔 add로 값 추가
3. set의 길이 len 으로 개수 출력

ㅡㅡㅡ
print(len(set(int(input()) % 42 for _ in range(10))))

순서 : int(input()) > set( input값 % 42 for~ ) > len() > print()

한 줄 짜리 풀이 
1. 10번 입력받으며 바로 % 42를 계산해서 리스트로 만듦
# 2. 그 리스트를 set()으로 감싸서 중복 제거
# 3. 그 길이를 len()으로 측정


