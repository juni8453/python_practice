def solution(age):
  my_list = list(str(age))
  answer = ''
  alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'u', 'w', 'x', 'y', 'z']

  for str_int in my_list:
    answer += alpa[int(str_int)]

  return answer