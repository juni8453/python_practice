def two(nums, target):
  nums.sort()
  n = len(nums)
  left = 0
  right = n - 1

  while left < right:
    if nums[left] + nums[right] > target:
      left += 1
    elif nums[left] + nums[right] < target:
      right -= 1
    elif nums[left] + nums[right] == target:
      return True
  return False

print(two(nums=[2,1,5,7], target=15))




