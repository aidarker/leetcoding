#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0028_实现strStr.py
@Time    :   2020-09-11
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


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        if not haystack:
            return -1

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == '__main__':
    start = time.time()
    
    sss = Solution()

    haystack = "hello"
    needle = "ll"
    result = sss.strStr(haystack, needle)
    print(result)

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))
