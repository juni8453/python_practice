# 계산 연산자
count = 0

count += 1
print(count)

count *= 2
print(count)

count += 3
count /= 2
print(count)

count -= 1
print(count)

# 논리 연산자
print(1 < 2)
print(2 < 1)
print('김' == '김')
print('김' == '이')

print(True and True)
print(True or True)
print(not True)
print(not False)
print(True or True)
print(True and False)

height = 120
age = 8
check = height > 140 and age > 10
print('청룡 열차를 탈 수 있을까?', end=' ')
print(check)

height = 150
age = 32
check = height > 140 and age > 10
print('청룡 열차를 탈 수 있을까?', end=' ')
print(check)

# Membership 연산자
list = ['Tany', 'Jerry', 'Nori', 'WitheEgg']
print('Hoo' in list)
print('Jun' in list)
print('Hoo' not in list)
print('Jun' not in list)