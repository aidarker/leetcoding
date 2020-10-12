#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0032.最长有效括号.py
@Time    :   2020-10-12
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


if __name__ == '__main__':
    start = time.time()
    
    
    
    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))