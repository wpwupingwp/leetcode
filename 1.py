# 1. Two Sum

from typing import List


def twoSum(nums: List[int], target: int):
    nums_d1 = dict()
    nums_d2 = dict()
    for index, n in enumerate(nums):
        if n not in nums_d1:
            nums_d1[n] = index
        else:
            nums_d2[n] = index
    for n in nums_d1:
        another = target - n
        if another in nums_d1:
            if n != another:
                return [nums_d1[n], nums_d1[another]]
            else:
                if another in nums_d2:
                    return [nums_d1[n], nums_d2[n]]


nums = [2, 7, 3, 3, 11, 15]
# target = 9
target = 6
print(twoSum(nums, target))
