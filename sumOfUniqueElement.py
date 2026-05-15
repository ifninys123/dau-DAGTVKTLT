class Solution(object):
    def sumOfUnique(self, nums):
        counts = Counter(nums)
        
        # 2. Tính tổng các số có số lần xuất hiện là 1
        total_sum = 0
        for num, count in counts.items():
            if count == 1:
                total_sum += num
                
        return total_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        