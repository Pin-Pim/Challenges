from typing import List

#This method of finding duplicates uses brute force but is very inefficient.
#When I tested it, it failed due to taking too long so I need to use some sort of sorting algorithm
#There's this thing I see a lot in LeetCode called the time complexity which is something like O(n).
#For example if I used a for loop in a for loop, it would have a value O(n^2).
#I think mine is a little different, a little more efficient then brute but would be sorta exponential in time complexity


'''
class Solution:
  def containsDuplicate(nums: List[int]) -> bool:
    secondList = []
    for number in nums:
      if number not in secondList:
        secondList.append(number)
      else:
        return True
    return False
  print(containsDuplicate([1,2,3,4,1]))
'''


#One sorting method that was mentioned said to organise the list into ascending order and check adjacent elements which would 
#have a time complexity of O(n log n).

'''
def containDuplicate(nums: List[int]) -> bool:
  nums.sort() #Sorts in ascending order. Not sure of the time complexity that it adds because I don't know the algorithm...
  print(nums)
  n = len(nums)
  for i in range(1,n):
    if nums[i] == nums[i-1]:
      return True
  return False
'''

'''
The hash set approach uses a hash set data structure to store encountered elements. It iterates through the array, checking if an element is already in the set. If so, it returns true. Otherwise, it adds the element to the set. This approach has a time complexity of O(n) and provides an efficient way to check for duplicates.
'''
