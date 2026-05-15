class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        res = [0] * n
        
        if k == 0:
            return res
        
        # Xác định phạm vi cửa sổ ban đầu
        if k > 0:
            start, end = 1, k
        else:
            start, end = n + k, n - 1
            
        current_sum = 0
        for i in range(start, end + 1):
            current_sum += code[i % n]
            
        for i in range(n):
            res[i] = current_sum
            current_sum -= code[start % n]
            start += 1
            end += 1
            current_sum += code[end % n]
            
        return res