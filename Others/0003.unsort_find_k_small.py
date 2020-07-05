#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0003.unsort_find_k_small.py
@Time    :   2020-07-04
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


def quickSortOneTime(nums, low, high):
    pivot = nums[low]
    while low<high:
        while low<high and pivot<nums[high]:
            high -= 1
        while low<high and pivot>nums[low]:
            low += 1
        temp = nums[low]
        nums[low] = nums[high]
        nums[high] = temp
    nums[low] = pivot
    return low


def findkth(nums, low, high, k):
    if low==high:
        return nums[low]
        
    index = quickSortOneTime(nums, low, high)
    if index==k:
        return nums[index]
    elif index<k:
        return findkth(nums, index+1, high, k)
    else:
        return findkth(nums, low, index-1, k)


if __name__ == '__main__':
    start = time.time()
    
    nums = [92, 5, 88, 13, 80, 70, 45]
    low, high = 0, len(nums)-1
    k=2
    result = findkth(nums, low, high, k)
    print("k:{}\tnums:{}\tindex:{}".format(k+1, result, nums.index(result)))
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))