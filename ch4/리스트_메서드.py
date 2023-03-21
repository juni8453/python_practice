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

# 값 추가 O(1)
list = [1,2,3,4,5,6]
list.append(7)
print(list)

# 특정 인덱스에 값 추가 O(N)
list = [1,2,3,4,5,6]
list.insert(1, 'a')
print(list)

# 내림차순 정렬 O(nlogN)
list = [1,2,3,4,5,6]
list.sort(reverse=True)
print(list)

# 원소 뒤집기 O(N)
list = [1, 2, 3, 4, 5, 6]
list.reverse()
print(list)

# 특정 값 개수 세기 O(N)
list = [1, 2, 3, 3, 4, 5, 6]
print(list.count(3))

# 특정 값 삭제 (여러 개라면 하나만 삭제) O(N)
list = [1, 2, 3, 3, 4, 5, 6]
list.remove(3)
print(list)

# 특정 값 모두 삭제 시 집합 자료형(set)과 섞어서 구현하면 좋다.
list = [1, 2, 3, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in list if i not in remove_set]
print(result)