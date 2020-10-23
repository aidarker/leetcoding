#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0034.在排序数组中查找元素的第一个和最后一个位置.py
@Time    :   2020-10-24
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
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        


if __name__ == '__main__':
    start = time.time()
    ssr = Solution()

    nums = [5,7,7,8,8,10]
    target = 8
    ssr.searchRange(nums, target)

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))