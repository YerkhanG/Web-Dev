def sum2(nums):
  sum = 0
  if(len(nums)==0):
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    sum += nums[0] + nums[1]
  return sum