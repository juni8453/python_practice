def solution1(my_string):
  answer = 0

  for i in my_string:
    ascii_code = ord(i)
    if 48 <= ascii_code <= 57:
      answer += int(i)
  return answer

def solution2(my_string):
  answer = 0

  for str in my_string:
    if str.isdigit():
      answer += int(str)

  return answer

def solution3(my_string):
  return sum(int(i) for i in my_string if i.isdigit())

print(solution1(my_string="aAb1B2cC34oOp"))
print(solution2(my_string="aAb1B2cC34oOp"))
print(solution3(my_string="aAb1B2cC34oOp"))