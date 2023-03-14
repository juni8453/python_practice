# while 조건:
#   실행할 명령1
#   실행할 명령2

# 기본 예제
count = 0
while count < 3:
  print('현재 roof 횟수:', count)
  count += 1

# continue, break 문 사용
count = 0
while count < 10:
  count += 1

  if count < 4:
    continue

  print('횟수:', count)

  if count == 8:
    break


count = 0
numbers = [1,2,3,4,5,6,7,8,9]

for index in range(len(numbers)):
  if index < 4:
    continue

  print('현재 index:', index)

  if index == 8:
    break
