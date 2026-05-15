class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
            
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Cập nhật giá mua thấp nhất tính đến thời điểm hiện tại
            if price < min_price:
                min_price = price
            # Hoặc tính toán lợi nhuận nếu bán ở ngày hiện tại
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit