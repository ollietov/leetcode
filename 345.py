class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        active = [letter for letter in s if letter in vowels]
        s_list = list(s)
        for i, letter in enumerate(s_list):
            if letter in vowels:
                s_list[i] = active.pop()
        return ''.join(s_list)