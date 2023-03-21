def twoSum(nums, target):
  data = dict()

  for key in nums: # O(N)
    data[key] = 1

  for key in nums: # O(N)
    if target - key in data: # O(1)
      return True
  return False

print(twoSum(nums=[4,1,9,7,5,3,16], target=14))
