import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_val = -sys.maxsize
min_val = sys.maxsize

def dfs(idx, value):
    global max_val, min_val
    
    if idx == N:
        max_val = max(max_val, value)
        min_val = min(min_val, value)
        return
    
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0: next_val = value + nums[idx]
            elif i == 1: next_val = value - nums[idx]
            elif i == 2: next_val = value * nums[idx]
            elif i == 3: next_val = int(value / nums[idx])
            dfs(idx + 1, next_val)
            ops[i] += 1

dfs(1, nums[0])
print(max_val)
print(min_val)