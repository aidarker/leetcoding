#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0001.binary_search.py
@Time    :   2020-06-24
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


def binary_search(arr, v):
    """ """
    low, high = 0, len(arr)
    while(low<high):
        mid = (low + high) // 2
        mid_value = arr[mid]
        if v == mid_value:
            return mid
        if mid_value > v:
            high = mid
        else:
            low = mid + 1
    return -1

if __name__ == '__main__':
    start = time.time()
    
    print(binary_search([1,2,3], 1))
    print(binary_search([1,1,2,3,4], 1))
    print(binary_search([1,2,3,4,6,7,8], 5))
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))