a_list = list(map(int, input().split()))
new_list = []

for i in range(1,9):
    new_list.append(i)
if a_list == new_list:
    print("ascending")
elif a_list == new_list[::-1]:
    print("descending")
else:
    print("mixed")
        