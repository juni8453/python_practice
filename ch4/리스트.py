list = []
print(list)

# append() 메서드를 사용해 값을 추가할 수 있다.
# 여러 개를 한 번에 넣을 수는 없다.
list.append(1)
print(list)

list.append('Tany')
print(list)

# insert() 메서드를 사용해 원하는 곳에 값을 추가할 수 있다.
list.insert(1, 'Jerry')
print(list)

# extend() 메서드를 사용해 다른 리스트끼리 합칠 수 있다.
new_list = ['apple', 'graph']
list.extend(new_list)
print(list)