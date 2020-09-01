#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0004.sequence_search.py
@Time    :   2020-08-27
@Author  :   KouKai
@Version :   V1.0
@Remarks :   时间复杂度 O(n)
'''

import sys
import os
path = os.getcwd()
path = os.path.dirname(path)
sys.path.append(path)

import time
import datetime
import logging


def sequence_search(arr, value):
    """ 顺序查找 """
    for i, v in enumerate(arr):
        if v == value:
            return i
    return -1


if __name__ == '__main__':
    start = time.time()
    
    arr = [1, 2, 3, 4]
    value = 3
    result = sequence_search(arr, value)
    print("result: {}".format(result))
    
    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))