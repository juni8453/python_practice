# 정렬
# sort() 사용 시 내부 값 타입이 모두 같아야 한다.
list = [123, 444]
list.sort()
print(list)

# 값이 몇 개 있는지 체크
# count()
animals = ['바다소', '코알라', '바다소', '아나콘다']
print(animals.count('바다소'))
print(animals.count('아나콘다'))
print(animals.count('아나콘'))
print(animals.count('코알라'))

# 내부에 값이 몇 개 있는지 ?
# len()
print(len(list), end=', ')
print(len(animals), end=', ')
print(len('str'))