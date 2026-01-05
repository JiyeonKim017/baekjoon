#  , 둘째 줄에 , 셋째 줄에 , 넷째 줄에 ((A%C) × (B%C))%C를4
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)