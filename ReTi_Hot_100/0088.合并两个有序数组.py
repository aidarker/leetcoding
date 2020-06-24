#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   88.合并两个有序数组.py
@Time    :   2020-06-22
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
import logging
logging.basicConfig(level = logging.INFO,format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m] + nums2[:n]
        t = sorted(temp)
        for i in range(len(t)):
            nums1[i] = t[i]
        return nums1


if __name__ == '__main__':
    start = time.time()
    
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    
    sm = Solution()
    result = sm.merge(nums1, m, nums2, n)
    print(result)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))