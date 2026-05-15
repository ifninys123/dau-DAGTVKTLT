class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)
        
        count = 0
        for num in nums:
            if min_val < num < max_val:
                count += 1
                
        return count