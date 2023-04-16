n = int(input())
grades = list(map(int, input().split()))
sum = 0
average = 0

# 최고 점수 구하기
max = max(grades)

# 점수 조작
for i in grades:
    sum += (i / max * 100)

# 조작된 점수의 평균 값
average = sum / n
print(average)
