#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0027.py
@Time    :   2020-08-27
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
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lenght = len(nums)
        i = 0
        while i<lenght:
            if nums[i] == val:
                del nums[i]
                lenght = len(nums)
                i=0
            else:
                i+=1
        
        return nums


if __name__ == '__main__':
    start = time.time()
    ret = Solution()

    nums = [3, 2, 2, 3]
    # nums = [3, 3]
    val = 3

    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # val = 3
    
    result = ret.removeElement(nums, val)
    print(result)

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))