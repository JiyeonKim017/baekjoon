import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    line = input().split()
    cmd = line[0]
    
    # 명령1
    if cmd == '1':
        stack.append(line[1])
        
    # 명령2
    elif cmd == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    # 명령3
    elif cmd == '3':
        print(len(stack))
        
    # 명령4
    elif cmd == '4':
        print(1 if not stack else 0)
    
    # 명령 5
    elif cmd == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)