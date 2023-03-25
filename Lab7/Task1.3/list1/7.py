def max_end3(nums):
  n = []
  if(nums[0] < nums[-1]):
    n.append(nums[-1])
    n.append(nums[-1])
    n.append(nums[-1])
  else:
    n.append(nums[0])
    n.append(nums[0])
    n.append(nums[0])
  return n