#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   08.py
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
import re
logging.basicConfig(level = logging.INFO,format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        return max(min(int(*re.findall('^[\\+\\-]?\\d+', s.lstrip())), 2**31 - 1), -2**31)


if __name__ == '__main__':
    start = time.time()
    
    s = " -000000000000000000004500"
    sma = Solution()
    result = sma.myAtoi(s)
    print("result : {}".format(result))

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))