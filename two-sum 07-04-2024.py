def twoSum(nums, target):
  numMap = {}
  n = len(nums)
  for i in range(n):
      numMap[nums[i]] = i
  for i in range(n):
     complement = target - nums[i]
     if complement in numMap and numMap[complement] != i:
        return [i, numMap[complement]]
  return []

  '''
  So apparently a hash table is the same as a dictionary in python which makes sense
  this would have a time complexity of n since it only loops through one for loop.
  '''