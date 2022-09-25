# -*- coding: utf-8 -*-
"""
Within a list, find the position of 2 elements that have a sum of target
"""


def twoSum(nums, target):
    first={}
    for i in range(len(nums)):
        item = nums[i]
        diff = target-item
        if diff in first:
            return print([first[diff], i])
        first[item] = i
        
twoSum(nums = [2,7,11,15], target = 9)
twoSum(nums = [3,2,4], target = 6)
twoSum(nums = [3,3], target = 6)
twoSum(nums = [2,2,6,4], target = 6)