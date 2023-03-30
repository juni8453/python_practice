data = input()
init = ''
count = 0

if data[0] == '1':
  init = '1'
else:
  init = '0'

# 기준을 잡아놨고, 1로 시작하는 경우와 0으로 시작하는 경우를 나눠준다.
if init == '0':
  # 0으로 시작하는 경우에는 1로 바뀌는 경우에만 count 해준다.
  for i in range(len(data) - 1):
    if data[i + 1] != data[i]:
      if data[i + 1] == '1' and data[i] == '0':
        count += 1

elif init == '1':
  # 1로 시작하는 경우에는 0으로 바뀌는 경우에 count
    for i in range(len(data) - 1):
      if data[i + 1] != data[i]:
        if data[i + 1] == '0' and data[i] == '1':
          count += 1

print(count)