#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   26_删除排序数组中的重复项.py
@Time    :   2020-06-05
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
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for value in nums:
            if value not in temp:
                temp.append(value)
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        return nums, len(temp)


if __name__ == '__main__':
    start = time.time()
    
    nums = [1, 1, 2]

    srd = Solution()
    result, lenght = srd.removeDuplicates(nums)
    print(result)
    print(lenght)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))