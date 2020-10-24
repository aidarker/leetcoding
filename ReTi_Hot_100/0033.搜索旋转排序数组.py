#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0033.py
@Time    :   2020-10-14
@Author  :   KouKai
@Version :   V1.0
@Remarks :   None
'''

import sys
import os
path = os.getcwd()
path = os.path.dirname(path)
sys.path.append(path)

import time
import datetime

class Solution(object):
    def binary_search(self, nums, target, left):
        """"""
        lo, hi = 0, len(nums)
        while lo<hi:
            mid = (lo + hi) // 2
            if nums[mid]>target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def search(self, nums, target):
        """ 利用二分查找思想+条件判断 """
        left_idx = self.binary_search(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        
        return [left_idx, self.binary_search(nums, target, False)-1]


if __name__ == '__main__':
    start = time.time()
    
    ss = Solution()
    nums = [5, 1, 3]
    target = 3
    result = ss.search(nums, target)
    print(result)

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))