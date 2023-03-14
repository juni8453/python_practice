import random

my_list = [1, 2, 3]
print(my_list)

# 그대로 프린트 가능
students = ['Tany', 'Dongi']
print(students)

# 반복문으로 하나씩 출력
for student in students: 
    print(student)

# 리스트 내 랜덤으로 선택 후 출력
print(random.choice(students))

# 리스트에 원소 추가 가능
students.append('Jerry')
for student in students:
    print(student)

# 리스트는 원소를 수정할 수 있다.
students[0] = 'Nori'

# 리스트와 비슷하지만 원소를 수정할 수 없다.
my_tuple = ('딸기', '포도', '바나나')
print(my_tuple)

# Dictionary 는 Map 과 비슷, key 값으로 value 값을 출력할 수 있다.
my_dict = {'Tany':'남', 'Dongi':'남', 'Hoo':'여'}
print(my_dict['Tany'])