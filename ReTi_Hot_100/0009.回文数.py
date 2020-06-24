#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   9_回文数.py
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
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)[::-1]
        if y == str(x):
            return True
        else:
            return False


if __name__ == '__main__':
    start = time.time()
    
    sip = Solution()
    x = 121
    result = sip.isPalindrome(x)
    print(result)    
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))