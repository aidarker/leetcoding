#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   75.颜色分类.py
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
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red_counter = 0
        white_counter = 0
        bule_counter = 0
        for num in nums:
            if num == 0:
                red_counter += 1
            elif num == 1:
                white_counter += 1
            elif num == 2:
                bule_counter += 1
        temp = red_counter*[0] + white_counter*[1] + bule_counter*[2]
        for i in range(len(temp)):
            nums[i] = temp[i]
        return nums


if __name__ == '__main__':
    start = time.time()
    
    nums = [2,0,2,1,1,0]
    ssc = Solution()
    result = ssc.sortColors(nums)
    print(result)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))