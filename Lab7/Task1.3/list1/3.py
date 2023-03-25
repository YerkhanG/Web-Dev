def reverse3(nums):
  n = []
  for i in range(1,len(nums)+1):
    n.append(nums[-i])
  return n
