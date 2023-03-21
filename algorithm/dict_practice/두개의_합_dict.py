def twoSum(nums, target):
  data = dict()

  for key in nums:
    data[key] = 1

  for key in nums:
    if target - key in data:
      return True
  return False

print(twoSum(nums=[4,1,9,7,5,3,16], target=14))
