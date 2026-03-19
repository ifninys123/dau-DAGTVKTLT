class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start_cities = set()
        for path in paths:
            start_cities.add(path[0])
        for path in paths:
            city_b = path[1]
            if city_b not in start_cities:
                return city_b
        