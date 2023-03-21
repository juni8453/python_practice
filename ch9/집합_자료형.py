# 집합 자료형 또한 중괄호를 사용하고 콤마를 기준으로 값을 넣으면 된다.
# set() 을 사용해서 초기화도 가능하다.
data = {1, 2, 3, 4, 4, 5}
print(data)

data2 = set([1, 2, 3, 4, 4, 5])
print(data2)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 교집합 &
print(a & b)

# 합집합 |
print(a | b)

# 차집합 -
print(a - b)

# 값 하나 추가 O(1)
a.add(6)
print(a)

# 값 여러 개 추가 O(1)
b.update([8, 9])
print(b)

# 특정한 값을 갖는 원소 삭제 O(1)
a.remove(6)
print(a)