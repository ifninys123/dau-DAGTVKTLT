class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        smaller_count_map = {}
    
        for i, num in enumerate(sorted_nums):
            if num not in smaller_count_map:
                smaller_count_map[num] = i
        return [smaller_count_map[num] for num in nums]
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        