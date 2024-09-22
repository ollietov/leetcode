class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)
        len2 = len(word2)
        merged = ''
        for i in range(max(len1,len2)):
            if i < len1:
                merged+=word1[i]
            if i < len2:
                merged+=word2[i]
        return merged