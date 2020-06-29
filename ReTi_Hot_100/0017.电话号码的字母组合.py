#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0017.电话号码的字母组合.py
@Time    :   2020-06-28
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
import numpy as np
logging.basicConfig(level = logging.INFO,format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        dic = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5':['j', 'k', 'l'],
                '6':['m', 'n', 'o'],
                '7':['p', 'q', 'r', 's'],
                '8':['t', 'u', 'v'],
                '9':['w', 'x', 'y', 'z']
            }
        
        arr = dic[digits[0]]
        t = []
        for i in digits[1:]:
            for j in arr:
                for k in dic[i]:
                    t.append(j+k)
            arr = t.copy()
        
        n = len(digits)
        t1 = []
        for k in arr:
            if len(k) == n:
                t1.append(k)
        return t1


if __name__ == '__main__':
    start = time.time()
    
    digits = "2345"
    slc = Solution()
    slc.letterCombinations(digits)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))