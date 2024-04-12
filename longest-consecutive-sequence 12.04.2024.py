class Solution(object):
    def longestConsecutive(self, nums):
        setitems = set(nums)
        maxcount = 0
        for x in setitems:
            if x -1 not in setitems:
                count = 1
                index = 1
                while x + index in setitems:
                    count +=1
                    index +=1
                if count > maxcount:
                    maxcount = count
        return maxcount            
        """
        :type nums: List[int]
        :rtype: int
        """