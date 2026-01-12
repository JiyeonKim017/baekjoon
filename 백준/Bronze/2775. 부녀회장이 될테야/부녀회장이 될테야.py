T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    floor = [i for i in range(1, n+1)]
    
    for _ in range(k):
        new_floor = []
        for j in range(1, n+1):
            new_floor.append(sum(floor[:j]))
        floor = new_floor
    print(floor[-1])