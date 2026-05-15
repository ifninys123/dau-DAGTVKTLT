class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        
        while left <= right:
            mid = left + (right - left) // 2
            current_coins = mid * (mid + 1) // 2
            
            if current_coins == n:
                return mid
            elif current_coins < n:
                left = mid + 1
            else:
                right = mid - 1
                
        return right