class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, number in enumerate(nums):
            for j, number2 in enumerate(nums[i+1:]):
                if number+number2 == target:
                    return [i,j+i+1]
