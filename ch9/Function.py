# def 함수이름(인자 1, ...)
#   실행 명령1
#   실행 명령2
#
#   return 결과

def add(numA, numB):
  return numA + numB

print(add(1,2))

def add_mul(numA, numB):
  return numA + numB, numA * numB

print(add_mul(1,2))

# 함수는 tuple 로 결과 값이 반환되기 때문에 패킹, 언패킹이 가능하다.
my_add, my_mul = add_mul(1, 2)
print(my_add)
print(my_mul)