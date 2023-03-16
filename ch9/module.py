import random

numbers = [1,2,3,4,5,6,7,8,9]
choice_num = random.choice(numbers)
print(choice_num)

members_numbers = [1,2,3,4]
members = {
  1 : 'Tany',
  2 : 'Yan',
  3 : 'Hanse',
  4 : 'Louie'
}

# choice() 랜덤으로 하나의 값을 받아낼 수 있다.
choice = random.choice(members_numbers)
print(members[choice])

# sample() 랜덤 으로 중복 없이 k 만큼의 값을 받아낼 수 있다.
print(random.sample(members_numbers, 2))
print(random.sample(range(1, 46), 6))

# randint() 숫자의 범위를 지정해서 범위 사이의 랜덤한 값을 받아낼 수 있다.
print(random.randint(8, 10))