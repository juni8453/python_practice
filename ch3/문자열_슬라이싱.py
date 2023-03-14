# substring 과 유사
str = "김왼손의 왼손코딩"
print(str[5:7])

# 앞, 뒤 및 두 값을 생략할 수도 있다.
print(str[:3])
print(str[2:])
print(str[:])

# split() 메서드 사용
# default 은 공백 기준
print(str.split()) # ['김왼손의', '왼손코딩']

fruit = "거봉 복숭아 바나나 토마토"
print(fruit.split()) # ['거봉', '복숭아', '바나나', '토마토']

name = "Tany:Dongi:Jerry:Nori"
print(name.split(":"))