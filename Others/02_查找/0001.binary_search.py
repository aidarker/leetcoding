#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0001.binary_search.py
@Time    :   2020-06-24
@Author  :   KouKai
@Version :   V1.0
@Remarks :   时间复杂度O(log(n))
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


def binary_search(arr, v):
    """ """
    low, high = 0, len(arr)
    while(low<high):
        mid = (low + high) // 2
        mid_value = arr[mid]
        if v < mid_value:
            high = mid
        elif v > mid_value:
            low = mid + 1
        else:
            return mid
    return -1


def binary_search_1(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        if target < mid_value:
            high = mid - 1
        elif target > mid_value:
            low = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    start = time.time()
    
    print(binary_search([1,2,3], 1))
    print(binary_search([1,1,2,3,4], 1))
    print(binary_search([1,2,3,4,6,7,8], 3))
    print(30*"==")
    print(binary_search_1([1,2,3], 1))
    print(binary_search_1([1,1,2,3,4], 1))
    print(binary_search_1([1,2,3,4,6,7,8], 3))
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))