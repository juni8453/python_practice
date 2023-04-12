n = int(input())
students = []
for i in range(n):
    data = input().split()
    students.append((data[0], int(data[1]), int(data[2]), int(data[3])))

# 국어 점수 내림차순 정렬
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])