# tuple 은 immutable 하기 때문에 값을 수정할 수 없다. (수정, 삭제 등)
# () 를 사용하지만 , 를 사용해 나열하면 tuple 로 만들 수 있다.
tuple = ('abc', 'def', 'ghi')
print(tuple)
print(tuple[0])
print(tuple[0:1])
print(tuple[0:2])
print(tuple[1:2])
print(type(tuple))

tuple2 = 'abc', 'def', 'ghi'
print(tuple2)
print(type(tuple2))