numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []

for num in numbers:
  if num % 2 == 1:
    odd_numbers.append(num)

print(odd_numbers)

# comprehension 을 사용해 간략하게 줄일 수 있다.
comprehension = [num for num in numbers if num % 2 == 1]
print(comprehension)