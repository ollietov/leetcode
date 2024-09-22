class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        max_candies = max(candies)
        for candy in candies:
            result.append(candy+extraCandies >= max_candies)
        return result