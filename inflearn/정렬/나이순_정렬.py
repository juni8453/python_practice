import sys

n = int(sys.stdin.readline())
age_name_list = []

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age_name_list.append([int(age), name])

age_name_list.sort(key=lambda x: x[0])

for age_name in age_name_list:
    print(f'{age_name[0]} {age_name[1]}')
