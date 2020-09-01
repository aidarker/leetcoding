#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0005.insertion_search.py
@Time    :   2020-08-27
@Author  :   KouKai
@Version :   V1.0
@Remarks :   时间复杂度 O(log(n))
'''

import sys
import os
path = os.getcwd()
path = os.path.dirname(path)
sys.path.append(path)

import time
import datetime
import logging


def insertion_search(arr, value):
    low, high = 0, len(arr)-1

    while (low<high):
        mid = low + (high - low) * (value - arr[low]) / (arr[high] - arr[low])
        if value < arr[mid]:
            high = mid - 1
        elif value > arr[mid]:
            low = mid + 1
        else:
            return mid


if __name__ == '__main__':
    start = time.time()
    
    arr = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    value = 7
    result = insertion_search(arr, value)
    print(result)

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))