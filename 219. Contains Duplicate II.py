class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        
        for i, num in enumerate(nums):
            # Nếu số này đã xuất hiện và khoảng cách chỉ số <= k
            if num in seen and i - seen[num] <= k:
                return True
            # Cập nhật chỉ số mới nhất của số hiện tại
            seen[num] = i
            
        return False