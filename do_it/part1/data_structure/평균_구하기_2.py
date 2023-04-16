n = int(input())
grades = list(map(int, input().split()))
max = max(grades)
sum = sum(grades)

print(sum * 100 / max / n)