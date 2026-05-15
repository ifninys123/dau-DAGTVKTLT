class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for num in nums:
            if abs(num) < abs(ans):
                ans = num
            elif abs(num) == abs(ans) and num > ans:
                ans = num
        return ans