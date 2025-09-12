def getX(x, nums):
  if x > len(nums) or nums == [] or x == 0:
    return 0
  else:
    nums.sort()
    i = nums[x-1]
    return i
