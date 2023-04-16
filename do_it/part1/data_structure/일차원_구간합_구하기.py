# 기준이 0 이 아닌 1 이기 때문에 n + 1 로 배열 설정

n, m = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
sum_list = [0] * (n + 1)

# 구간 합 배열 설정
for i in range(1, n + 1):
    sum_list[i] = sum_list[i - 1] + numbers[i]

# 구간 합 구하기
for i in range(m):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start - 1])
