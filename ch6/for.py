# 파이썬 for 는 띄워 쓰기가 필수
fruits = ['apple', 'banana', 'tomato']
for fruit in fruits:
  print(fruit)

nums = [1, 2, 3]
for num in nums:
  print(num)

strs = 'tomato'
for str in strs:
  print(str)

scores = [90, 85, 77, 65, 97]
cheating_list = set([2, 4])

for i in range(5):
  if i + 1 in cheating_list:
    continue
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")
