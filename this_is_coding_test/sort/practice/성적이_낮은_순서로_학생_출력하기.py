from operator import itemgetter

n = int(input())
array = []

for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

sorted_list = sorted(array, key=itemgetter(1))

for student in sorted_list:
    print(student[0], end=' ')
