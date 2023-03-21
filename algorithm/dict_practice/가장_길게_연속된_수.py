def longestConsecutive(nums):
  longest = 0
  num_dict = {}

  for num in nums:
    num_dict[num] = True

  for num in num_dict:
    # 현재 숫자의 이전 값을 찾을 수 없다면 연속 수의 첫 원소 값이다.
    # 해당 조건문이 없다면 이미 연속 수를 계산할 떄 포함된 값을 다시 중복 계산하기 때문에 걸러줘야 함.
    if num - 1 not in num_dict:
      count = 1
      next_num = num + 1
      while next_num in num_dict:
        count += 1
        next_num += 1
        longest = max(longest, count)
  return longest

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1,1]))
