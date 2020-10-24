#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0034. 在排序数组中查找元素的第一个和最后一个位置.py
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
    def searchRange(self, nums, target):
        """ """
        low, high = 0, len(nums)
        while(low<high):
            mid = (low + high) // 2
            mid_value = nums[mid]
            if target == mid_value:
                return [mid, mid]

            if mid_value > target:
                high = mid
            else:
                low = mid + 1
                
        return [-1, -1]


if __name__ == '__main__':
    start = time.time()
    
    ssr = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    ssr.searchRange(nums, target)
    
    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))