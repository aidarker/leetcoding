#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   dtw.py
@Time    :   2020-06-19
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
import numpy as np

def distance(xi, yi):
    return abs(xi - yi)


def dtw(A, B, d = lambda x,y: abs(x-y)):
    A, B = np.array(A), np.array(B)
    M, N = len(A), len(B)
    cost = np.zeros((M, N))
    cost[0, 0] = d(A[0], B[0])

    for i in range(1, M):
        cost[i, 0] = cost[i-1, 0] + d(A[i], B[0])
    
    for j in range(1, N):
        cost[0, j] = cost[0, j-1] + d(A[0], B[j])

    for i in range(1, M):
        for j in range(1, N):
            choices = cost[i-1, j], cost[i, j-1], cost[i-1, j-1]
            cost[i, j] = d(A[i], B[j]) + min(choices)

    print(cost[-1, -1])

    
if __name__ == '__main__':
    start = time.time()
    
    A=[1,1,1,2,10,3]
    B=[1,1,1,10,2,3]
    
    dtw(A, B)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))