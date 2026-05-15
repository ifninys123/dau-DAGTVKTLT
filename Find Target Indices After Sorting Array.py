class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        less_than = 0
        
        for num in nums:
            if num == target:
                count += 1
            elif num < target:
                less_than += 1
                
        return [i for i in range(less_than, less_than + count)]