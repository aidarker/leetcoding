#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0006.fibonacci_search.py
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


def fibonacci_search(arr, value):
    """ """
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]
    low, high = 0, len(arr)-1

    k = 0
    while (high > F[k]-1):
        k += 1
    
    i = high
    while (F[k]-1 > i):
        arr.append(arr[high])
        i += 1
    
    while (low<high):
        if k < 2:
            mid = low
        else:
            mid = low + F[k-1] - 1
        
        if value < arr[mid]:
            high = mid - 1
            k -= 1
        elif value > arr[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                return mid
            else:
                return high



if __name__ == '__main__':
    start = time.time()
    
    arr = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    value = 7
    result = fibonacci_search(arr, value)
    print(result)

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))