class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        clean = number.replace(" ", "").replace("-", "")
        res = []
        i = 0
        n = len(clean)
        
        while n - i > 4:
            res.append(clean[i:i+3])
            i += 3
            
        if n - i == 4:
            res.append(clean[i:i+2])
            res.append(clean[i+2:i+4])
        else:
            res.append(clean[i:])
            
        return "-".join(res)
        """
        :type number: str
        :rtype: str
        """