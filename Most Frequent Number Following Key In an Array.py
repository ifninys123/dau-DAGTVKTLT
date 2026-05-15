class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        counts = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                counts[target] = counts.get(target, 0) + 1
                
        max_count = -1
        ans = -1
        for target, count in counts.items():
            if count > max_count:
                max_count = count
                ans = target
                
        return ans