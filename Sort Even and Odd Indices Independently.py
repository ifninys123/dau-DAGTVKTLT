class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = sorted([nums[i] for i in range(0, len(nums), 2)])
        odd = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True)
        
        res = []
        for i in range(len(even)):
            res.append(even[i])
            if i < len(odd):
                res.append(odd[i])
                
        return res