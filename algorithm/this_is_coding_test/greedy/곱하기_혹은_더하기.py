n = input()
answer = 1

for i in list(n):
  if int(i) > 1:
    answer *= int(i)

  # 0 or 1 일 때는 더하는게 더 효율적
  elif int(i) <= 1:
    answer += int(i)

print(answer)