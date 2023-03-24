import math

def solution(n):
  my_dict = dict()
  my_result = dict()

  for i in range(1, n + 1):
    my_dict[i] = True

  for key in my_dict:
    x = math.trunc(n / key)

    # key 와 곱해서 n 이 나오는 x 값이 존재하면,
    if x in my_dict and (n % key) == 0 :
      my_result[key] = x

  size = len(my_result)
  print(size)

print(solution(100))