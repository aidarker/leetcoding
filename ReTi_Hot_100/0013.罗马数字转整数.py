#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   13_罗马数字转整数.py
@Time    :   2020-06-05
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


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        temp = []
        for i, n in enumerate(s):
            temp.append(d.get(s[max(i-1, 0): i+1], d[n]))
        return sum(temp)


if __name__ == '__main__':
    start = time.time()
    
    s = "IVIIX"
    srt = Solution()
    result = srt.romanToInt(s)
    print(result)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))