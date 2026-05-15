class Solution(object):
    def twoSum(self, nums, target):
        indexOf={}
        for i in range (len(nums)):
            index = i
            number=nums[i]
            indexOf[number] = index
        for i in range (len(nums)):
            x=target-nums[i]
            if x in indexOf:
                return indexOf[x],i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        