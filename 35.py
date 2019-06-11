import unittest

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums) - 1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return right



