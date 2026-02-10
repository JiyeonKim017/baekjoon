def solution(participant, completion):
    answer = ''
    hash_dict = {}
    
    for p in participant:
        hash_dict[p] = hash_dict.get(p, 0) + 1
    
    for c in completion:
        if c in hash_dict:
            hash_dict[c] -= 1
    
    for answer in hash_dict:
        if hash_dict[answer] > 0:
            return answer

    return answer



# def solution(participant, completion):
#     answer = ''
#     hash_dict = {}
    
#     for p in participant:
#         if p in hash_dict:
#             hash_dict[p] += 1
#         else:
#             hash_dict[p] = 1
    
#     for c in completion:
#         if c in hash_dict:
#             hash_dict[c] -= 1
    
#     for answer in hash_dict:
#         if hash_dict[answer] > 0:
#             return answer

#     return answer