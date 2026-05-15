class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        
        for val in arr:
            # Kiểm tra xem gấp đôi giá trị hiện tại hoặc một nửa giá trị hiện tại đã xuất hiện chưa
            if 2 * val in seen or (val % 2 == 0 and val // 2 in seen):
                return True
            seen.add(val)
            
        return False