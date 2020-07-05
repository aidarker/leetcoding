#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0002.unsort_find_k.py
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
    poivt = nums[low]
    while low < high:
        while low<high and poivt < nums[high]: high -= 1
        while low<high and poivt > nums[low]: low +=1
        
        temp = nums[low]
        nums[low] = nums[high]
        nums[high] = temp
    
    nums[high] = poivt
    return high
            
def findKth(nums, low, high, k):
    index = 0
    if (low==high):
        return nums[low]
    
    partition = quickSortOneTime(nums, low, high)
    index = high-partition+1
    if (index==k):
        return nums[partition]
    elif index<k:
        return findKth(nums, low, partition-1, k-index)
    else:
        return findKth(nums, partition+1, high, k)


if __name__ == '__main__':
    start = time.time()
    
    nums = [92, 5, 88, 13, 80, 70, 45]
    low, high = 0, len(nums)-1
    k = 4
    result = findKth(nums, low, high, k)
    print("k:{}\tnum:{}\tindex:{}".format(k, result, nums.index(result)))
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))