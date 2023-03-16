dict = {}
dict[0] = 'a'
print(dict) # key : 0, value : 'a'

dict['b'] = 2
print(dict) # key : 'b', value : '2'

dict['학생 1'] = 'Tany'
print(dict) # key : '학생 1', value : 'Tany'

# key 를 가지고 value 값을 가져올 수 있다.
print(dict[0])
print(dict['b'])
print(dict['학생 1'])

# del 키워드로 key 값을 지울 수 있다.
del dict[0]
del dict['b']
print(dict)

# Dictionary 메서드
dict['학생 2'] = 'Nori'
dict['학생 3'] = 'Hoo'

# Key 값 출력 (default)
for student in dict:
  print(student)

for student in dict.keys():
  print(student)

# Value 값 출력
for student in dict.values():
  print(student)

# Key, Value 한번에 출력
for key, value in dict.items():
  print(key, value)