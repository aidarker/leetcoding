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
logging.basicConfig(level = logging.INFO,format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        print(digits)


if __name__ == '__main__':
    start = time.time()
    
    digits = "23"
    slc = Solution()
    slc.letterCombinations(digits)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))