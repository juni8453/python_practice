def solution1(hp):
  count = 0

  ant_types = [5, 3, 1]

  # 그리디 적용
  for type in ant_types:
    count += hp // type
    hp %= type

  return count

print(solution1(23))
print(solution1(24))
print(solution1(999))