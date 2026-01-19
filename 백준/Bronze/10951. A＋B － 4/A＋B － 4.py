import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)
    
# sys.stdin : 읽을 데이터 통로가 되어줌. 값이 없을 때까지 라는 조건이 자연스레 붙게 됨.
# .readline()은 한 줄만 불러와줌.