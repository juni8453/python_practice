# 패킹
tuple = 1, 2, 3

# 언패킹
num1, num2, num3 = tuple
print(num1)
print(num2)
print(num3)

# 이렇게 값을 서로 바꿔줄 수도 있다.
num1, num2 = num2, num1 # 1,2 = 2,1
print(num1) # 2
print(num2) # 1