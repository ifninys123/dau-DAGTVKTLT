class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        rule_map = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        index_to_check = rule_map[ruleKey]
        count = 0
        
        # 2. Duyệt qua từng item và so sánh
        for item in items:
            if item[index_to_check] == ruleValue:
                count += 1
                
        return count
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        